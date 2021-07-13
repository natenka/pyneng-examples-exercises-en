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
    if sys.modules.get("task_6_2a"):
        del sys.modules["task_6_2a"]
    import task_6_2a

    out, err = capsys.readouterr()
    correct_stdout = ip_type
    assert (
        out
    ), "Nothing is printed to stdout. It is necessary not only to get the correct result, but also to print it to the stdout using print"
    assert correct_stdout in out.strip(), "Wrong output is printed to stdout"


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
    monkeypatch.setattr("builtins.input", lambda x=None: ip_add)
    if sys.modules.get("task_6_2a"):
        del sys.modules["task_6_2a"]
    import task_6_2a

    out, err = capsys.readouterr()
    correct_stdout = ip_type
    assert (
        out
    ), "Nothing is printed to stdout. It is necessary not only to get the correct result, but also to print it to the stdout using print"
    assert correct_stdout == out.strip().lower(), "Wrong output is printed to stdout"
