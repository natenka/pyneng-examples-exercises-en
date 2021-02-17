import pytest
import task_18_3
import sys

sys.path.append("..")

from pyneng_common_functions import (
    check_function_exists,
    check_function_params,
    strip_empty_lines,
)

# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def test_functions_created():
    """
    Checking that the function has been created
    """
    check_function_exists(task_18_3, "send_commands")


def test_function_params(r1_test_connection, first_router_from_devices_yaml):
    show_command = "sh ip int br"
    cfg_commands = ["logging buffered 20010"]
    with pytest.raises(TypeError) as excinfo:
        # if show/config arguments are not passed as keyword arguments,
        # a TypeError exception should be raised
        task_18_3.send_commands(first_router_from_devices_yaml, show_command)

    with pytest.raises(ValueError) as excinfo:
        # If both show and config are passed, a ValueError exception should be raised
        task_18_3.send_commands(
            first_router_from_devices_yaml, show=show_command, config=cfg_commands
        )


def test_function_return_value(r1_test_connection, first_router_from_devices_yaml):
    """
    Function check
    """
    show_command = "sh ip int br"
    cfg_commands = [
        "logging 10.255.255.1",
        "logging buffered 20010",
        "no logging console",
    ]
    correct_return_value_show = r1_test_connection.send_command(show_command)
    correct_return_value_cfg = r1_test_connection.send_config_set(cfg_commands)
    return_value_show = task_18_3.send_commands(
        first_router_from_devices_yaml, show=show_command
    )
    return_value_cfg = task_18_3.send_commands(
        first_router_from_devices_yaml, config=cfg_commands
    )
    assert return_value_show != None, "The function returns None"
    assert (
        type(return_value_show) == str
    ), f"The function must return string, and it returns a {type(return_value).__name__}"
    assert strip_empty_lines(correct_return_value_show) == strip_empty_lines(
        return_value_show
    ), "Function returns wrong value for show command"
    assert strip_empty_lines(correct_return_value_cfg) == strip_empty_lines(
        return_value_cfg
    ), "Function returns wrong value config commands"
