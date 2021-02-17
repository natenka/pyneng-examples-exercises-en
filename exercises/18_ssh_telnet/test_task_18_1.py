import pytest
import task_18_1
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
    check_function_exists(task_18_1, "send_show_command")


def test_function_return_value(r1_test_connection, first_router_from_devices_yaml):
    """
    first_router_from_devices_yaml - is the first device from the devices.yaml file
    r1_test_connection - is the SSH session with the first device from the
    devices.yaml file. Used to check the output
    """
    correct_return_value = r1_test_connection.send_command("sh ip int br")
    return_value = task_18_1.send_show_command(
        first_router_from_devices_yaml, "sh ip int br"
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
    correct_return_value = r1_test_connection.send_command("sh int description")
    return_value = task_18_1.send_show_command(
        first_router_from_devices_yaml, "sh int description"
    )
    assert return_value != None, "The function returns None"
    assert (
        type(return_value) == str
    ), f"The function must return string, and it returns a {type(return_value).__name__}"
    assert strip_empty_lines(return_value) == strip_empty_lines(
        correct_return_value
    ), "Function returns wrong value"
