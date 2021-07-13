import csv
import inspect
from platform import system as system_name
from subprocess import run, PIPE
from concurrent.futures import ThreadPoolExecutor
import re
import os
from jinja2 import Environment, FileSystemLoader
import yaml
import textfsm


stdout_incorrect_warning = """
The message is different from the one specified in the task.
Should be: {}
And output: {}
"""


def unified_columns_output(output):
    output = delete_empty_lines(output)
    lines = [re.split(r"  +", line.strip()) for line in output.strip().split("\n")]
    formatted = [("{:25}" * len(line)).format(*line) for line in lines]
    return "\n".join(formatted)


def delete_empty_lines(output):
    output = output.replace("\r\n", "\n")
    lines = []
    for line in output.strip().split("\n"):
        if line.strip():
            lines.append(line.rstrip())
    return "\n".join(lines)


def check_attr_or_method(obj, attr=None, method=None):
    if attr:
        assert getattr(obj, attr, None) != None, "Variable not found"
        assert not inspect.ismethod(
            getattr(obj, attr)
        ), f"{attr} must be a variable, not a method"
    if method:
        assert getattr(obj, method, None) != None, "Method not found"
        assert inspect.ismethod(
            getattr(obj, method)
        ), f"{method} must be a method, not a variable"


def strip_empty_lines(output):
    output = output.replace("\r\n", "\n")
    lines = []
    for line in output.strip().split("\n"):
        line = line.strip()
        if line:
            lines.append(re.sub(" +", " ", line.strip()))
    return "\n".join(lines)


def check_class_exists(module, class_name):
    assert hasattr(module, class_name) and inspect.isclass(
        getattr(module, class_name)
    ), f"You need to create a class named {class_name}"


def check_function_exists(module, function_name):
    assert hasattr(module, function_name) and inspect.isfunction(
        getattr(module, function_name)
    ), f"You need to create a function named {function_name}"


def check_function_params(function, param_count, param_names=None):
    arg_info = inspect.getfullargspec(function)
    assert (
        len(arg_info.args) == param_count
    ), f"The {function.__name__} function must have {param_count} parameters"
    if param_names:
        assert set(arg_info.args) == set(
            param_names
        ), f"The function must have the following parameters: {','.join(param_names)}"


def get_func_params_default_value(function):
    func_sig = inspect.signature(function)
    return {
        k: v.default
        for k, v in func_sig.parameters.items()
        if v.default is not inspect.Parameter.empty
    }


def ping(host):
    param = "-n" if system_name().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]
    reply = run(command, stdout=PIPE, encoding="utf-8")
    return reply.returncode == 0


def get_reach_unreach(list_of_ips):
    with ThreadPoolExecutor(max_workers=4) as executor:
        f_result = list(executor.map(ping, list_of_ips))
    ip_status_map = dict(zip(list_of_ips, f_result))
    reachable = [ip for ip, status in ip_status_map.items() if status]
    unreachable = [ip for ip, status in ip_status_map.items() if not status]
    return reachable, unreachable


def read_all_csv_content_as_list(csv_filename):
    with open(csv_filename) as f:
        reader = csv.reader(f)
        return list(reader)


def unify_topology_dict(topology_dict):
    unified_topology_dict = {
        min(key, value): max(key, value) for key, value in topology_dict.items()
    }
    return unified_topology_dict


def render_jinja_template(template, data_dict):
    templ_dir, templ_file = os.path.split(template)
    env = Environment(
        loader=FileSystemLoader(templ_dir), trim_blocks=True, lstrip_blocks=True
    )
    templ = env.get_template(templ_file)
    return templ.render(data_dict)


def get_textfsm_output(template, command_output):
    with open(template) as tmpl:
        parser = textfsm.TextFSM(tmpl)
        header = parser.header
        result = parser.ParseText(command_output)
    return [header] + result
