import pytest
import task_18_1a
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists

# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def test_functions_created():
    """
    Checking that the function has been created
    """
    check_function_exists(task_18_1a, "send_show_command")


def test_function_return_value(capsys, first_router_wrong_pass):
    """
    Function check
    """
    return_value = task_18_1a.send_show_command(first_router_wrong_pass, "sh ip int br")
    correct_stdout = "authentication"
    out, err = capsys.readouterr()
    assert out != "", "Error message not printed to stdout"
    assert correct_stdout in out.lower(), "Wrong error message printed"
