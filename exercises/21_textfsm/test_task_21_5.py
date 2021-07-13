import textfsm
import os
import pytest
import task_21_5
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists

# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def test_functions_created():
    """
    Checking that the function has been created
    """
    check_function_exists(task_21_5, "send_and_parse_command_parallel")


def test_function_return_value(r1_test_connection, first_router_from_devices_yaml):
    """
    Function check
    """
    with open("templates/sh_ip_int_br.template") as f:
        re_table = textfsm.TextFSM(f)
    sh_ip_int_br = r1_test_connection.send_command("sh ip int br")
    result = re_table.ParseText(sh_ip_int_br)
    correct_return_value = {
        first_router_from_devices_yaml["host"]: [
            dict(zip(re_table.header, line)) for line in result
        ]
    }

    full_pth = os.path.join(os.getcwd(), "templates")
    return_value = task_21_5.send_and_parse_command_parallel(
        [first_router_from_devices_yaml], "sh ip int br", templates_path=full_pth
    )

    assert return_value != None, "The function returns None"
    assert (
        type(return_value) == dict
    ), f"The function should return a dict, instead it returns a {type(return_value).__name__}"
    assert correct_return_value == return_value, "Function returns wrong value"
