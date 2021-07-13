import pytest


# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def test_task_stdout(capsys):
    """
    Task check
    """
    import task_4_4

    out, err = capsys.readouterr()
    correct_stdout = "[1, 2, 3, 4, 10, 20, 30, 100]"
    assert (
        out
    ), "Nothing is printed to stdout. It is necessary not only to get the correct result, but also to print it to the stdout using print"
    assert correct_stdout == out.strip(), "Wrong line is printed to stdout"


def test_task_variables():
    """
    Checking that the required variable has been created
    in the task and contains the correct result
    """
    import task_4_4

    # variables created in the task:
    task_vars = [var for var in dir(task_4_4) if not var.startswith("_")]

    correct_result = [1, 2, 3, 4, 10, 20, 30, 100]
    assert "result" in task_vars, "List should be written to the result variable"
    assert (
        type(task_4_4.result) == list
    ), f"The result variable must contain a list, not a {type(task_4_4.result).__name__}"
    assert (
        correct_result == task_4_4.result
    ), f"The result variable must be a list {correct_result}"
