import pytest
import task_15_5
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists

# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def test_function_created():
    """
    Checking that the function has been created
    """
    check_function_exists(task_15_5, "generate_description_from_cdp")


def test_function_return_value():
    """
    Function check
    """
    correct_return_value = {
        "Eth 0/1": "description Connected to R1 port Eth 0/0",
        "Eth 0/2": "description Connected to R2 port Eth 0/0",
        "Eth 0/3": "description Connected to R3 port Eth 0/0",
        "Eth 0/5": "description Connected to R6 port Eth 0/1",
    }
    return_value = task_15_5.generate_description_from_cdp("sh_cdp_n_sw1.txt")
    assert return_value != None, "The function returns None"
    assert (
        type(return_value) == dict
    ), f"The function should return a dict, instead it returns a {type(return_value).__name__}"
    assert (
        return_value == correct_return_value
    ), "Function returns wrong value"
