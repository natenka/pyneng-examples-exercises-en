from importlib import reload
import sys
import pytest


# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def test_task_r2(capsys, monkeypatch):
    """
    Task check for r2
    """
    monkeypatch.setattr("builtins.input", lambda x=None: "r2")
    import task_5_1

    out, err = capsys.readouterr()
    r2_dict = {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    }

    assert (
        out
    ), "Nothing is printed to stdout. It is necessary not only to get the correct result, but also to print it to the stdout using printprint"
    assert (
        str(r2_dict) in out.strip()
    ), "Wrong output is printed to stdout"


def test_task_sw1(capsys, monkeypatch):
    """
    Task check for sw1
    """
    monkeypatch.setattr("builtins.input", lambda x=None: "sw1")
    if sys.modules.get("task_5_1"):
        reload(sys.modules["task_5_1"])
    import task_5_1

    out, err = capsys.readouterr()
    sw1_dict = {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    }
    assert (
        out
    ), "Nothing is printed to stdout. It is necessary not only to get the correct result, but also to print it to the stdout using printprint"
    assert (
        str(sw1_dict) in out.strip()
    ), "Wrong output is printed to stdout"
