import pytest
import task_9_4
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists, check_function_params

# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def test_function_created():
    """
    Checking that the function has been created
    """
    check_function_exists(task_9_4, "convert_config_to_dict")


def test_function_params():
    """
    Checking names and number of parameters
    """
    check_function_params(
        function=task_9_4.convert_config_to_dict,
        param_count=1,
        param_names=["config_filename"],
    )


def test_function_return_value():
    """
    Function check
    """
    correct_return_value = {
        "version 15.0": [],
        "service timestamps debug datetime msec": [],
        "service timestamps log datetime msec": [],
        "no service password-encryption": [],
        "hostname sw1": [],
        "interface FastEthernet0/0": [
            "switchport mode access",
            "switchport access vlan 10",
        ],
        "interface FastEthernet0/1": [
            "switchport trunk encapsulation dot1q",
            "switchport trunk allowed vlan 100,200",
            "switchport mode trunk",
        ],
        "interface FastEthernet0/2": [
            "switchport mode access",
            "switchport access vlan 20",
        ],
        "interface FastEthernet0/3": [
            "switchport trunk encapsulation dot1q",
            "switchport trunk allowed vlan 100,300,400,500,600",
            "switchport mode trunk",
        ],
        "interface FastEthernet1/0": [
            "switchport mode access",
            "switchport access vlan 20",
        ],
        "interface FastEthernet1/1": [
            "switchport mode access",
            "switchport access vlan 30",
        ],
        "interface FastEthernet1/2": [
            "switchport trunk encapsulation dot1q",
            "switchport trunk allowed vlan 400,500,600",
            "switchport mode trunk",
        ],
        "interface FastEthernet1/3": [],
        "interface Vlan100": ["ip address 10.0.100.1 255.255.255.0"],
        "line con 0": ["exec-timeout 0 0", "privilege level 15", "logging synchronous"],
        "line aux 0": [],
        "line vty 0 4": ["login", "transport input all"],
        "end": [],
    }

    return_value = task_9_4.convert_config_to_dict("config_sw1.txt")
    assert return_value != None, "The function returns None"
    assert (
        type(return_value) == dict
    ), f"The function should return a dict, instead it returns a {type(return_value).__name__}"
    assert (
        return_value == correct_return_value
    ), "Function returns wrong value"
