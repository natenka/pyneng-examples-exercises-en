import re
import pytest


# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def unified_columns_output(output):
    lines = [re.split(r"  +", line.strip()) for line in output.strip().split("\n")]
    formatted = [("{:25}"*len(line)).format(*line) for line in lines]
    return "\n".join(formatted)


def test_task_stdout(capsys):
    """
    Task check
    """
    import task_4_6

    out, err = capsys.readouterr()
    correct_stdout = unified_columns_output(
        "Prefix                10.0.24.0/24\n"
        "AD/Metric             110/41\n"
        "Next-Hop              10.0.13.3\n"
        "Last update           3d18h\n"
        "Outbound Interface    FastEthernet0/0\n"
    )
    assert (
        out
    ), "Nothing is printed to stdout. It is necessary not only to get the correct result, but also to print it to the stdout using printprint"
    assert (
        unified_columns_output(out.strip()) == correct_stdout
    ), "Wrong line is printed to stdout"
