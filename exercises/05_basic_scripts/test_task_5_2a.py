import re
from importlib import reload
import pytest
import sys

sys.path.append("..")

from pyneng_common_functions import unified_columns_output


# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def test_task_10_5_5_1_24(capsys, monkeypatch):
    """
    Task check for 10.5.5.1/24
    """
    monkeypatch.setattr("builtins.input", lambda x=None: "10.5.5.1/24")
    import task_5_2a

    out, err = capsys.readouterr()
    stdout = unified_columns_output(out.strip())
    correct_stdout = unified_columns_output(
        "Network:\n"
        "10        5         5         0\n"
        "00001010  00000101  00000101  00000000\n\n"
        "Mask:\n"
        "/24\n"
        "255       255       255       0\n"
        "11111111  11111111  11111111  00000000"
    )

    assert (
        out
    ), "Nothing is printed to stdout. It is necessary not only to get the correct result, but also to print it to the stdout using print"
    assert correct_stdout == stdout, "Wrong output printed"


def test_task_10_1_1_193_28(capsys, monkeypatch):
    """
    Task check for 10.1.1.193/28
    """
    monkeypatch.setattr("builtins.input", lambda x=None: "10.1.1.193/28")
    if sys.modules.get("task_5_2a"):
        reload(sys.modules["task_5_2a"])
    import task_5_2a

    out, err = capsys.readouterr()
    stdout = unified_columns_output(out.strip())
    correct_stdout = unified_columns_output(
        "Network:\n"
        "10        1         1         192\n"
        "00001010  00000001  00000001  11000000\n\n"
        "Mask:\n"
        "/28\n"
        "255       255       255       240\n"
        "11111111  11111111  11111111  11110000"
    )

    assert (
        out
    ), "Nothing is printed to stdout. It is necessary not only to get the correct result, but also to print it to the stdout using print"
    assert correct_stdout == stdout, "Wrong output printed"


def test_task_172_16_100_237_29(capsys, monkeypatch):
    """
    Task check for 172.16.100.237/29
    """
    monkeypatch.setattr("builtins.input", lambda x=None: "172.16.100.237/29")
    if sys.modules.get("task_5_2a"):
        reload(sys.modules["task_5_2a"])
    import task_5_2a

    out, err = capsys.readouterr()
    stdout = unified_columns_output(out.strip())
    correct_stdout = unified_columns_output(
        "Network:\n"
        "172       16        100       232\n"
        "10101100  00010000  01100100  11101000\n\n"
        "Mask:\n"
        "/29\n"
        "255       255       255       248\n"
        "11111111  11111111  11111111  11111000"
    )

    assert (
        out
    ), "Nothing is printed to stdout. It is necessary not only to get the correct result, but also to print it to the stdout using print"
    assert correct_stdout == stdout, "Wrong output printed"
