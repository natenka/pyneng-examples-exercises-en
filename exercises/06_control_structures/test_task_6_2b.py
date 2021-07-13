from functools import wraps
from importlib import reload
import sys
import pytest


# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


@pytest.mark.parametrize(
    "ip_add,ip_type",
    [
        ("10.1.1.1", "unicast"),
        ("230.1.1.1", "multicast"),
        ("255.255.255.255", "local broadcast"),
        ("0.0.0.0", "unassigned"),
        ("250.1.1.1", "unused"),
    ],
)
def test_task_correct_ip(capsys, monkeypatch, ip_add, ip_type):
    monkeypatch.setattr("builtins.input", lambda x=None: ip_add)
    if sys.modules.get("task_6_2b"):
        del sys.modules["task_6_2b"]
    import task_6_2b

    out, err = capsys.readouterr()
    correct_stdout = ip_type
    assert (
        out
    ), "Nothing is printed to stdout. It is necessary not only to get the correct result, but also to print it to the stdout using print"
    assert correct_stdout in out.strip(), "Wrong output is printed to stdout"


def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        __tracebackhide__ = True
        wrapper.total_calls += 1
        result = func(*args, **kwargs)
        return result

    wrapper.total_calls = 0
    return wrapper


def monkey_input_ip(ip_add):
    __tracebackhide__ = True

    @count_calls
    def inner(prompt):
        __tracebackhide__ = True
        if inner.total_calls == 1:
            return ip_add
        elif inner.total_calls == 2:
            return "10.1.1.1"

    return inner


@pytest.mark.parametrize(
    "ip_add,ip_type",
    [
        ("10.1.1", "invalid ip address"),
        ("10.a.2.a", "invalid ip address"),
        ("10.1.1.1.1", "invalid ip address"),
        ("10.1.1.", "invalid ip address"),
        ("300.1.1.1", "invalid ip address"),
        ("30,1.1.1.1", "invalid ip address"),
    ],
)
def test_task_wrong_ip(capsys, monkeypatch, ip_add, ip_type):
    monkeypatch.setattr("builtins.input", monkey_input_ip(ip_add))
    if sys.modules.get("task_6_2b"):
        del sys.modules["task_6_2b"]
    import task_6_2b

    out, err = capsys.readouterr()
    correct_stdout = ip_type + "\nunicast"
    assert (
        out
    ), "Nothing is printed to stdout. It is necessary not only to get the correct result, but also to print it to the stdout using print"
    assert correct_stdout == out.strip().lower(), "Wrong output is printed to stdout"
