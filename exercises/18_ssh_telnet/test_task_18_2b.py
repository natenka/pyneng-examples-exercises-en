import re

import yaml
import pytest
import task_18_2b
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists

# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


correct_return_value = (
    {
        "ip http server": "config term\n"
        "Enter configuration commands, one per line.  End with CNTL/Z.\n"
        "R1(config)#ip http server\n"
        "R1(config)#",
        "logging buffered 20010": "config term\n"
        "Enter configuration commands, one per line.  End with CNTL/Z.\n"
        "R1(config)#logging buffered 20010\n"
        "R1(config)#",
    },
    {
        "a": "config term\n"
        "Enter configuration commands, one per line.  End with CNTL/Z.\n"
        "R1(config)#a\n"
        '% Ambiguous command:  "a"\n'
        "R1(config)#",
        "logging": "config term\n"
        "Enter configuration commands, one per line.  End with CNTL/Z.\n"
        "R1(config)#logging\n"
        "% Incomplete command.\n"
        "\n"
        "R1(config)#",
        "logging 0255.255.1": "config term\n"
        "Enter configuration commands, one per line.  End with CNTL/Z.\n"
        "R1(config)#logging 0255.255.1\n"
        "                   ^\n"
        "% Invalid input detected at '^' marker.\n"
        "\n"
        "R1(config)#",
    },
)


def test_functions_created():
    """
    Checking that the function has been created
    """
    check_function_exists(task_18_2b, "send_config_commands")


def test_function_return_value(capsys, first_router_from_devices_yaml):
    """
    Function check
    """
    commands_with_errors = ["logging 0255.255.1", "logging", "a"]
    correct_commands = ["logging buffered 20010", "ip http server"]
    test_commands = commands_with_errors + correct_commands

    return_value = task_18_2b.send_config_commands(
        first_router_from_devices_yaml, test_commands, log=False
    )

    assert return_value != None, "The function returns None"
    assert type(return_value) == tuple, "The function must return a tuple"
    assert 2 == len(return_value) and all(
        type(item) == dict for item in return_value
    ), "The function must return a tuple with two dicts"
    correct_good, correct_bad = correct_return_value
    return_good, return_bad = return_value
    assert (
        correct_good.keys() == return_good.keys()
    ), "Function returns wrong value for a dictionary with no errors"
    assert (
        correct_bad.keys() == return_bad.keys()
    ), "Function returns wrong value for a dictionary with commands with errors"


@pytest.mark.parametrize(
    "error,command",
    [
        ("Invalid input detected", "logging 0255.255.1"),
        ("Incomplete command", "logging"),
        ("Ambiguous command", "a"),
    ],
)
def test_function_stdout(error, command, capsys, first_router_from_devices_yaml):
    return_value = task_18_2b.send_config_commands(
        first_router_from_devices_yaml, [command], log=False
    )

    stdout, err = capsys.readouterr()
    ip = first_router_from_devices_yaml["host"]
    assert error in stdout, "The error message does not contain the error itself"
    assert command in stdout, "There is no command in the error message"
    assert (
        ip in stdout
    ), "The error message does not contain the IP address of the device"
