import pytest
import task_19_1
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists, get_reach_unreach

# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def test_functions_created():
    """
    Checking that the function has been created
    """
    check_function_exists(task_19_1, "ping_ip_addresses")


def test_function_return_value():
    """
    Function check
    """
    list_of_ips = ["1.1.1.1", "8.8.8.8", "8.8.4.4", "2.2.2.2"]
    correct_return_value = get_reach_unreach(list_of_ips)
    correct_reachable, correct_unreachable = correct_return_value
    correct_reachable, correct_unreachable = sorted(correct_reachable), sorted(
        correct_unreachable
    )

    return_value = task_19_1.ping_ip_addresses(list_of_ips)
    assert return_value != None, "The function returns None"
    assert (
        type(return_value) == tuple
    ), f"The function should return a tuple, instead it returns a {type(return_value).__name__}"
    assert 2 == len(return_value), "The function must return a tuple with two lists"
    return_reachable, return_unreachable = return_value

    assert all(
        type(item) == list for item in return_value
    ), "The function must return a tuple with lists"
    return_reachable, return_unreachable = return_value
    return_reachable, return_unreachable = sorted(return_reachable), sorted(
        return_unreachable
    )
    assert correct_return_value == (return_value), "Function returns wrong value"
