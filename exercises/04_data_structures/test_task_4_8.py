import re
import pytest


# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def unified_columns_output(output):
    lines = [re.split(r" +", line.strip()) for line in output.strip().split("\n")]
    formatted = [("{:10}"*len(line)).format(*line) for line in lines]
    return "\n".join(formatted)


def test_task_stdout(capsys):
    """
    Task check
    """
    import task_4_8

    out, err = capsys.readouterr()
    correct_stdout = unified_columns_output(
        "192       168       3         1\n"
        "11000000  10101000  00000011  00000001\n"
    )
    assert (
        out
    ), "Nothing is printed to stdout. It is necessary not only to get the correct result, but also to print it to the stdout using printprint"
    assert (
        unified_columns_output(out.strip()) == correct_stdout
    ), "Wrong line is printed to stdout"
