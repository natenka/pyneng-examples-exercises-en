import pytest
import task_9_3
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
    check_function_exists(task_9_3, "get_int_vlan_map")


def test_function_params():
    """
    Checking names and number of parameters
    """
    check_function_params(
        function=task_9_3.get_int_vlan_map,
        param_count=1,
        param_names=["config_filename"],
    )


def test_function_return_value():
    """
    Function check
    """
    correct_return_value = (
        {
            "FastEthernet0/0": 10,
            "FastEthernet0/2": 20,
            "FastEthernet1/0": 20,
            "FastEthernet1/1": 30,
        },
        {
            "FastEthernet0/1": [100, 200],
            "FastEthernet0/3": [100, 300, 400, 500, 600],
            "FastEthernet1/2": [400, 500, 600],
        },
    )

    return_value = task_9_3.get_int_vlan_map("config_sw1.txt")
    assert return_value != None, "The function returns None"
    assert (
        type(return_value) == tuple
    ), f"The function should return a tuple, instead it returns a {type(return_value).__name__}"
    assert len(return_value) == 2 and all(
        type(item) == dict for item in return_value
    ), "The function must return a tuple with two dicts"

    access, trunk = return_value
    assert correct_return_value == return_value, "Function returns wrong value"
