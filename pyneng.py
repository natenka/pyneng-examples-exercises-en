import sys
import subprocess
import re
import os
from collections import defaultdict
import json
import pathlib
import stat
import shutil
from glob import glob

import click
import pytest
from pytest_jsonreport.plugin import JSONReport


task_dirs = [
    "04_data_structures",
    "05_basic_scripts",
    "06_control_structures",
    "07_files",
    "09_functions",
    "11_modules",
    "12_useful_modules",
    "15_module_re",
    "17_serialization",
    "18_ssh_telnet",
    "19_concurrent_connections",
    "20_jinja2",
    "21_textfsm",
    "22_oop_basics",
    "23_oop_special_methods",
    "24_oop_inheritance",
]


class PynengError(Exception):
    """
    Error in the use/operation of the pyneng script
    """


def red(msg):
    return click.style(msg, fg="red")


def green(msg):
    return click.style(msg, fg="green")


def exception_handler(exception_type, exception, traceback):
    """
    sys.excepthook to disable traceback output by default
    """
    print(f"\n{exception_type.__name__}: {exception}\n")


class CustomTasksType(click.ParamType):
    """
    The class creates a new type for click and converts the valid choices
    of the assignment strings into separate test files.

    In addition, it checks if there is such a file in the current directory
    and leaves only those that are.
    """

    def convert(self, value, param, ctx):
        regex = (
            r"(?P<all>all)|"
            r"(?P<number_star>\d\*)|"
            r"(?P<letters_range>\d[a-i]-[a-i])|"
            r"(?P<numbers_range>\d-\d)|"
            r"(?P<single_task>\d[a-i]?)"
        )
        current_chapter = current_dir_name()
        if current_chapter not in task_dirs:
            task_dirs_line = "\n    ".join(task_dirs)
            self.fail(
                red(
                    f"\nThe script must be called from the task directories:"
                    f"\n    {task_dirs_line}"
                )
            )

        current_chapter = current_chapter_id()
        tasks_list = re.split(r"[ ,]+", value)
        test_files = []
        for task in tasks_list:
            match = re.fullmatch(regex, task)
            if match:
                if task == "all":
                    return value
                else:
                    if match.group("letters_range"):
                        task = f"{task[0]}[{task[1:]}]"  # convert 1a-c to 1[a-c]
                    elif match.group("numbers_range"):
                        task = f"[{task}]"  # convert 1-3 to [1-3]

                    test_files += glob(f"test_task_{current_chapter}_{task}.py")
            else:
                self.fail(
                    red(
                        f"This format is not supported {task}. "
                        "Supported formats: 1, 1a, 1b-d, 1*, 1-3"
                    )
                )
        return test_files


def call_command(command, verbose=True, return_stdout=False, return_stderr=False):
    """
    The function calls the specified command via subprocess and prints stdout
    and stderr if verbose=True.
    """
    result = subprocess.run(
        command,
        shell=True,
        encoding="utf-8",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    std = result.stdout
    stderr = result.stderr
    if return_stdout:
        return std
    if return_stderr:
        return result.returncode, stderr
    if verbose:
        print("#" * 20, command)
        if std:
            print(std)
        if stderr:
            print(stderr)
    return result.returncode


def current_chapter_id():
    """
    The function returns the number of the current section where pyneng is called.
    """
    pth = str(pathlib.Path().absolute())
    last_dir = os.path.split(pth)[-1]
    current_chapter = int(last_dir.split("_")[0])
    return current_chapter


def current_dir_name():
    pth = str(pathlib.Path().absolute())
    current_chapter_name = os.path.split(pth)[-1]
    return current_chapter_name


def parse_json_report(report):
    """
    Selects parts from the pytest run report in JSON format.
    Returns a list of passedd tests.
    """
    if report and report["summary"]["total"] != 0:
        all_tests = defaultdict(list)
        summary = report["summary"]

        test_names = [test["nodeid"] for test in report["collectors"][0]["result"]]
        for test in report["tests"]:
            name = test["nodeid"].split("::")[0]
            all_tests[name].append(test["outcome"] == "passed")
        all_passed_tasks = [name for name, outcome in all_tests.items() if all(outcome)]
        return all_passed_tasks
    else:
        return []


def copy_answers(passed_tasks):
    """
    The function clones the repository with answers to the user's home
    directory and copies the answers for the tasks that passed the tests.
    After the answers are copied, the repository with the answers is deleted.
    All of this is done manually, not through tempfile, due to deletion
    issues on Windows.
    """
    pth = str(pathlib.Path().absolute())
    current_chapter_name = os.path.split(pth)[-1]
    current_chapter_number = int(current_chapter_name.split("_")[0])

    homedir = pathlib.Path.home()
    os.chdir(homedir)
    if os.path.exists("pyneng-answers"):
        shutil.rmtree("pyneng-answers", onerror=remove_readonly)
    returncode, stderr = call_command(
        "git clone --depth=1 https://github.com/natenka/pyneng-answers",
        verbose=False,
        return_stderr=True,
    )
    if returncode == 0:
        os.chdir(f"pyneng-answers-en/answers/{current_chapter_name}")
        copy_answer_files(passed_tasks, pth)
        print(
            green(
                "\nThe answers to the tasks that passed the tests "
                "are copied to the files answer_task_x.py\n"
            )
        )
        os.chdir(homedir)
        shutil.rmtree("pyneng-answers-en", onerror=remove_readonly)
    else:
        if "could not resolve host" in stderr.lower():
            raise PynengError(
                red(
                    "Failed to copy answers. Perhaps there is no internet access?"
                )
            )
        else:
            raise PynengError(red("Failed to copy answers."))
    os.chdir(pth)


def remove_readonly(func, path, _):
    """
    Helper function for Windows that allows to remove read only files
    from the .git directory
    """
    os.chmod(path, stat.S_IWRITE)
    func(path)


def copy_answer_files(passed_tasks, pth):
    """
    The function copies the answers for the specified tasks.
    """
    for test_file in passed_tasks:
        task_name = test_file.replace("test_", "")
        task_name = re.search(r"task_\w+\.py", task_name).group()
        answer_name = test_file.replace("test_", "answer_")
        answer_name = re.search(r"answer_task_\w+\.py", answer_name).group()
        if not os.path.exists(f"{pth}/{answer_name}"):
            shutil.copy2(task_name, f"{pth}/{answer_name}")


@click.command(
    context_settings=dict(
        ignore_unknown_options=True, help_option_names=["-h", "--help"]
    )
)
@click.argument("tasks", default="all", type=CustomTasksType())
@click.option(
    "--disable-verbose", "-d", is_flag=True, help="Disable pytest verbose output"
)
@click.option(
    "--answer",
    "-a",
    is_flag=True,
    help=(
        "Copy answers for assignments that passed the tests. "
        "When this flag is added, no traceback is displayed for tests."
    ),
)
@click.option("--debug", is_flag=True, help="Show traceback")
def cli(tasks, disable_verbose, answer, debug):
    """
    Run tests for TASKS. By default, all tests will run.

    Examples of running pyneng:

    \b
        pyneng            run all tests for current chapter
        pyneng 1,2a,5     run tests for tasks 1, 2a и 5
        pyneng 1,2a-c,5   run tests for tasks 1, 2a, 2b, 2c и 5
        pyneng 1,2*       run tests for tasks 1, all tasks 2
        pyneng 1,3-5      run tests for tasks 1, 3, 4, 5
        pyneng 1-5 -a     run test and get answers

    The -d flag disables verbose output from pytest, which is enabled by default.
    The -a flag writes answers to the answer_task_x.py files if the tests pass.
    """
    if not debug:
        sys.excepthook = exception_handler

    json_plugin = JSONReport()
    pytest_args_common = ["--json-report-file=none", "--disable-warnings"]

    if disable_verbose:
        pytest_args = [*pytest_args_common, "--tb=short"]
    else:
        pytest_args = [*pytest_args_common, "-vv"]

    if answer:
        pytest_args = [*pytest_args_common, "--tb=no"]

    if tasks == "all":
        pytest.main(pytest_args, plugins=[json_plugin])
    else:
        pytest.main(tasks + pytest_args, plugins=[json_plugin])

    passed_tasks = parse_json_report(json_plugin.report)

    if passed_tasks and answer:
        copy_answers(passed_tasks)


if __name__ == "__main__":
    cli()
