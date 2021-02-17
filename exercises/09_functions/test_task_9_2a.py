import pytest
import task_9_2a
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
    check_function_exists(task_9_2a, "generate_trunk_config")


def test_function_params():
    """
    Checking names and number of parameters
    """
    check_function_params(
        function=task_9_2a.generate_trunk_config,
        param_count=2,
        param_names=["intf_vlan_mapping", "trunk_template"],
    )


def test_function_return_value():
    """
    Function check
    """
    trunk_vlans_mapping = {
        "FastEthernet0/1": [10, 20, 30],
        "FastEthernet0/2": [11, 30],
        "FastEthernet0/4": [17],
    }
    template_trunk_mode = [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan",
    ]
    correct_return_value = {
        "FastEthernet0/1": [
            "switchport mode trunk",
            "switchport trunk native vlan 999",
            "switchport trunk allowed vlan 10,20,30",
        ],
        "FastEthernet0/2": [
            "switchport mode trunk",
            "switchport trunk native vlan 999",
            "switchport trunk allowed vlan 11,30",
        ],
        "FastEthernet0/4": [
            "switchport mode trunk",
            "switchport trunk native vlan 999",
            "switchport trunk allowed vlan 17",
        ],
    }

    return_value = task_9_2a.generate_trunk_config(
        trunk_vlans_mapping, template_trunk_mode
    )
    assert return_value != None, "The function returns None"
    assert (
        type(return_value) == dict
    ), f"The function should return a dict, instead it returns a {type(return_value).__name__}"
    assert (
        return_value == correct_return_value
    ), "Function returns wrong value"
