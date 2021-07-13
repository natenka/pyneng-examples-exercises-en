import pytest
import task_12_2
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
    check_function_exists(task_12_2, "convert_ranges_to_ip_list")


def test_function_return_value():
    """
    Function check
    """
    list_of_ips_and_ranges = ["8.8.4.4", "1.1.1.1-3", "172.21.41.128-172.21.41.132"]
    correct_return_value = [
        "8.8.4.4",
        "1.1.1.1",
        "1.1.1.2",
        "1.1.1.3",
        "172.21.41.128",
        "172.21.41.129",
        "172.21.41.130",
        "172.21.41.131",
        "172.21.41.132",
    ]

    return_value = task_12_2.convert_ranges_to_ip_list(list_of_ips_and_ranges)
    assert return_value != None, "The function returns None"
    assert type(return_value) == list, "The function should return a list"
    assert sorted(correct_return_value) == sorted(
        return_value
    ), "Function returns wrong value"


def test_function_return_value_different_args():
    list_of_ips_and_ranges = ["10.1.1.1", "10.4.10.10-13", "192.168.1.12-192.168.1.15"]
    correct_return_value = [
        "10.1.1.1",
        "10.4.10.10",
        "10.4.10.11",
        "10.4.10.12",
        "10.4.10.13",
        "192.168.1.12",
        "192.168.1.13",
        "192.168.1.14",
        "192.168.1.15",
    ]

    return_value = task_12_2.convert_ranges_to_ip_list(list_of_ips_and_ranges)
    assert return_value != None, "The function returns None"
    assert (
        type(return_value) == list
    ), f"The function should return a list, instead it returns a {type(return_value).__name__}"
    assert sorted(correct_return_value) == sorted(
        return_value
    ), "Function returns wrong value"
