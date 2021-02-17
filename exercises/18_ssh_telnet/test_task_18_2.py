import pytest
import task_18_2
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists, strip_empty_lines

# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def test_functions_created():
    """
    Checking that the function has been created
    """
    check_function_exists(task_18_2, "send_config_commands")


def test_function_return_value(r1_test_connection, first_router_from_devices_yaml):
    """
    Function check
    """
    test_commands = [
        "logging 10.255.255.1",
        "logging buffered 20010",
        "no logging console",
    ]
    correct_return_value = r1_test_connection.send_config_set(test_commands)
    return_value = task_18_2.send_config_commands(
        first_router_from_devices_yaml, test_commands
    )
    assert return_value != None, "The function returns None"
    assert (
        type(return_value) == str
    ), f"The function must return string, and it returns a {type(return_value).__name__}"
    assert strip_empty_lines(return_value) == strip_empty_lines(
        correct_return_value
    ), "Function returns wrong value"


def test_function_return_value_different_args(
    r1_test_connection, first_router_from_devices_yaml
):
    """
    Checking the function with different arguments
    """
    test_commands = [
        "interface Loopback 100",
        "ip address 10.1.1.100 255.255.255.255",
    ]
    correct_return_value = r1_test_connection.send_config_set(test_commands)
    return_value = task_18_2.send_config_commands(
        first_router_from_devices_yaml, test_commands
    )
    assert return_value != None, "The function returns None"
    assert (
        type(return_value) == str
    ), f"The function must return string, and it returns a {type(return_value).__name__}"
    assert strip_empty_lines(return_value) == strip_empty_lines(
        correct_return_value
    ), "Function returns wrong value"
