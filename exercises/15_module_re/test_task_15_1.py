import pytest
import task_15_1
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
    check_function_exists(task_15_1, "get_ip_from_cfg")


def test_function_return_value():
    """
    Function check
    """
    correct_return_value = [
        ("10.1.1.1", "255.255.255.255"),
        ("10.0.13.1", "255.255.255.0"),
        ("10.0.19.1", "255.255.255.0"),
    ]

    return_value = task_15_1.get_ip_from_cfg("config_r1.txt")
    assert return_value != None, "The function returns None"
    assert (
        type(return_value) == list
    ), f"The function should return a list, instead it returns a {type(return_value).__name__}"
    # The lists are sorted so that there is no error if the addresses are written
    # in the list in a different order. In this task, the order of the tuples
    # in the list is not important.
    assert sorted(correct_return_value) == sorted(
        return_value
    ), "Function returns wrong value"


def test_function_return_value_different_args():
    """
    Checking the function with different arguments
    """
    correct_return_value = [
        ("10.3.3.3", "255.255.255.255"),
        ("10.0.13.3", "255.255.255.0"),
    ]

    return_value = task_15_1.get_ip_from_cfg("config_r3.txt")
    assert return_value != None, "The function returns None"
    assert (
        type(return_value) == list
    ), f"The function should return a list, instead it returns a {type(return_value).__name__}"
    assert sorted(correct_return_value) == sorted(
        return_value
    ), "Function returns wrong value"
