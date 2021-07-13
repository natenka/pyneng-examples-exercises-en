import re
import pytest
import sys

sys.path.append("..")

from pyneng_common_functions import unified_columns_output


# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def test_task_stdout(capsys):
    """
    Task check
    """
    import task_4_8

    out, err = capsys.readouterr()
    correct_stdout = unified_columns_output(
        "192       168       3         1\n" "11000000  10101000  00000011  00000001\n"
    )
    assert (
        out
    ), "Nothing is printed to stdout. It is necessary not only to get the correct result, but also to print it to the stdout using print"
    assert correct_stdout == unified_columns_output(
        out.strip()
    ), "Wrong line is printed to stdout"
