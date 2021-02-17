import pytest
import task_15_2a
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
    check_function_exists(task_15_2a, "convert_to_dict")


def test_function_return_value():
    """
    Function check
    """
    headers = ["hostname", "ios", "platform"]
    parsed_data = [
        ("R1", "12.4(24)T1", "Cisco 3825"),
        ("R2", "15.2(2)T1", "Cisco 2911"),
        ("SW1", "12.2(55)SE9", "Cisco WS-C2960-8TC-L"),
    ]
    correct_return_value = [
        {"hostname": "R1", "ios": "12.4(24)T1", "platform": "Cisco 3825"},
        {"hostname": "R2", "ios": "15.2(2)T1", "platform": "Cisco 2911"},
        {"hostname": "SW1", "ios": "12.2(55)SE9", "platform": "Cisco WS-C2960-8TC-L"},
    ]
    return_value = task_15_2a.convert_to_dict(headers, parsed_data)
    assert return_value != None, "The function returns None"
    assert (
        type(return_value) == list
    ), f"The function should return a list, instead it returns a {type(return_value).__name__}"
    assert (
        return_value == correct_return_value
    ), "Function returns wrong value"


def test_function_return_value_different_args():
    """
    Checking the function with different arguments
    """
    parsed_sh_ip_int_br = [
        ("FastEthernet0/0", "15.0.15.1", "up", "up"),
        ("FastEthernet0/1", "10.0.12.1", "up", "up"),
        ("FastEthernet0/2", "10.0.13.1", "up", "up"),
        ("FastEthernet0/3", "unassigned", "administratively down", "down"),
        ("Loopback0", "10.1.1.1", "up", "up"),
        ("Loopback100", "100.0.0.1", "up", "up"),
    ]

    correct_return_value = [
        {
            "interface": "FastEthernet0/0",
            "address": "15.0.15.1",
            "status": "up",
            "protocol": "up",
        },
        {
            "interface": "FastEthernet0/1",
            "address": "10.0.12.1",
            "status": "up",
            "protocol": "up",
        },
        {
            "interface": "FastEthernet0/2",
            "address": "10.0.13.1",
            "status": "up",
            "protocol": "up",
        },
        {
            "interface": "FastEthernet0/3",
            "address": "unassigned",
            "status": "administratively down",
            "protocol": "down",
        },
        {
            "interface": "Loopback0",
            "address": "10.1.1.1",
            "status": "up",
            "protocol": "up",
        },
        {
            "interface": "Loopback100",
            "address": "100.0.0.1",
            "status": "up",
            "protocol": "up",
        },
    ]

    headers = ["interface", "address", "status", "protocol"]
    return_value = task_15_2a.convert_to_dict(headers, parsed_sh_ip_int_br)
    assert return_value != None, "The function returns None"
    assert (
        type(return_value) == list
    ), f"The function should return a list, instead it returns a {type(return_value).__name__}"
    assert (
        return_value == correct_return_value
    ), "Function returns wrong value"
