import os
import pytest
import task_22_2c
import sys

sys.path.append("..")

from pyneng_common_functions import check_class_exists, check_attr_or_method, strip_empty_lines

# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def test_class_created():
    """
    Checking that the class has been created
    """
    check_class_exists(task_22_2c, "CiscoTelnet")


def test_send_config_commands_correct_commands(first_router_from_devices_yaml, capsys):
    r1 = task_22_2c.CiscoTelnet(**first_router_from_devices_yaml)
    check_attr_or_method(r1, method="send_config_commands")

    correct_commands = ["interface loop55", "ip address 5.5.5.5 255.255.255.255"]
    return_value = r1.send_config_commands(correct_commands)
    assert (
        correct_commands[0] in return_value and correct_commands[1] in return_value
    ), "send_config_commands method returns wrong value"


@pytest.mark.parametrize(
    "error,command",
    [
        ("Invalid input detected", "logging 0255.255.1"),
        ("Incomplete command", "logging"),
        ("Ambiguous command", "a"),
    ],
)
def test_send_config_commands_wrong_commands(
    first_router_from_devices_yaml, capsys, error, command
):
    r1 = task_22_2c.CiscoTelnet(**first_router_from_devices_yaml)

    return_value = r1.send_config_commands(command, strict=False)
    out, err = capsys.readouterr()
    assert error in out, "send_config_commands method does not print error message"

    with pytest.raises(ValueError) as excinfo:
        return_value = r1.send_config_commands(command, strict=True)
    assert error in str(
        excinfo
    ), "send_config_commands method should raise exception when strict=True"
