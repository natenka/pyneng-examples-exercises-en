import pytest
import task_15_1b
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
    check_function_exists(task_15_1b, "get_ip_from_cfg")


def test_function_return_value():
    """
    Function check
    """
    correct_return_value = {
        "Loopback0": [("10.2.2.2", "255.255.255.255")],
        "Ethernet0/0": [("10.0.23.2", "255.255.255.0")],
        "Ethernet0/1": [
            ("10.255.2.2", "255.255.255.0"),
            ("10.254.2.2", "255.255.255.0"),
        ],
        "Ethernet0/2": [("10.0.29.2", "255.255.255.0")],
    }

    return_value = task_15_1b.get_ip_from_cfg("config_r2.txt")
    assert return_value != None, "The function returns None"
    assert (
        type(return_value) == dict
    ), f"The function should return a dict, instead it returns a {type(return_value).__name__}"
    assert correct_return_value == return_value, "Function returns wrong value"
