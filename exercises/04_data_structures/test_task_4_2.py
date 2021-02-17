import pytest


# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def test_task_stdout(capsys):
    """
    Task check
    """
    import task_4_2

    out, err = capsys.readouterr()
    correct_stdout = (
        "AAAA.BBBB.CCCC"
    )
    assert (
        out
    ), "Nothing is printed to stdout. It is necessary not only to get the correct result, but also to print it to the stdout using printprint"
    assert (
        out.strip() == correct_stdout
    ), "Wrong line is printed to stdout"
