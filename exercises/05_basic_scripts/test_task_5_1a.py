from functools import wraps
from importlib import reload
import sys
import pytest


# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        __tracebackhide__ = True
        wrapper.total_calls += 1
        result = func(*args, **kwargs)
        return result

    wrapper.total_calls = 0
    return wrapper


@count_calls
def monkey_input_r2(prompt):
    __tracebackhide__ = True
    if monkey_input_r2.total_calls == 1:
        return "r2"
    elif monkey_input_r2.total_calls == 2:
        return "ip"


@count_calls
def monkey_input_sw1(prompt):
    __tracebackhide__ = True
    if monkey_input_sw1.total_calls == 1:
        return "sw1"
    elif monkey_input_sw1.total_calls == 2:
        return "ios"


def test_task_r2(capsys, monkeypatch):
    """
    Task check for r2
    """
    monkeypatch.setattr("builtins.input", monkey_input_r2)
    import task_5_1a

    out, err = capsys.readouterr()
    correct_stdout = "10.255.0.2"

    assert (
        out
    ), "Nothing is printed to stdout. It is necessary not only to get the correct result, but also to print it to the stdout using print"
    assert correct_stdout in out.strip(), "Wrong output is printed to stdout"


def test_task_sw1(capsys, monkeypatch):
    """
    Task check for sw1
    """
    monkeypatch.setattr("builtins.input", monkey_input_sw1)
    if sys.modules.get("task_5_1a"):
        reload(sys.modules["task_5_1a"])
    import task_5_1a

    out, err = capsys.readouterr()
    correct_stdout = "3.6.XE"
    assert (
        out
    ), "Nothing is printed to stdout. It is necessary not only to get the correct result, but also to print it to the stdout using print"
    assert correct_stdout in out.strip(), "Wrong output is printed to stdout"
