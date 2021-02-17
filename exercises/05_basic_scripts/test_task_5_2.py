import re
from importlib import reload
import sys
import pytest


# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def unified_columns_output(output):
    lines = [re.split(r" +", line.strip()) for line in output.strip().split("\n")]
    formatted = [("{:10}"*len(line)).format(*line) for line in lines]
    return "\n".join(formatted)


def test_task_10_5_5_0_24(capsys, monkeypatch):
    """
    Task check for 10.5.5.0/24
    """
    monkeypatch.setattr("builtins.input", lambda x=None: "10.5.5.0/24")
    import task_5_2

    out, err = capsys.readouterr()
    stdout = unified_columns_output(out.strip())
    correct_stdout_network = unified_columns_output(
        "10        5         5         0\n"
        "00001010  00000101  00000101  00000000"
    )

    correct_stdout_mask = unified_columns_output(
        "/24\n"
        "255       255       255       0\n"
        "11111111  11111111  11111111  00000000"
    )

    assert (
        out
    ), "Nothing is printed to stdout. It is necessary not only to get the correct result, but also to print it to the stdout using printprint"
    assert (
        correct_stdout_network in stdout
    ), "Wrong network value printed"
    assert (
        correct_stdout_mask in stdout
    ), "Wrong mask value printed"


def test_task_10_1_1_192_28(capsys, monkeypatch):
    """
    Task check for 10.1.1.192/28
    """
    monkeypatch.setattr("builtins.input", lambda x=None: "10.1.1.192/28")
    if sys.modules.get("task_5_2"):
        reload(sys.modules["task_5_2"])
    import task_5_2

    out, err = capsys.readouterr()
    stdout = unified_columns_output(out.strip())
    correct_stdout_network = unified_columns_output(
        "10        1         1         192\n"
        "00001010  00000001  00000001  11000000"
    )

    correct_stdout_mask = unified_columns_output(
        "/28\n"
        "255       255       255       240\n"
        "11111111  11111111  11111111  11110000"
    )

    assert (
        out
    ), "Nothing is printed to stdout. It is necessary not only to get the correct result, but also to print it to the stdout using printprint"
    assert (
        correct_stdout_network in stdout
    ), "Wrong network value printed"
    assert (
        correct_stdout_mask in stdout
    ), "Wrong mask value printed"


