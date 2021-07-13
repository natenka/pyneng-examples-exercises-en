import pytest
import task_11_2
import glob
import sys

sys.path.append("..")

from pyneng_common_functions import (
    check_function_exists,
    check_function_params,
    unify_topology_dict,
)

# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def test_function_created():
    """
    Checking that the function has been created
    """
    check_function_exists(task_11_2, "create_network_map")


def test_function_params():
    """
    Checking names and number of parameters
    """
    check_function_params(
        function=task_11_2.create_network_map, param_count=1, param_names=["filenames"]
    )


def test_function_return_value():
    """
    Function check
    """
    correct_return_value = {
        ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
        ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
        ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
        ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
        ("R3", "Eth0/1"): ("R4", "Eth0/0"),
        ("R3", "Eth0/2"): ("R5", "Eth0/0"),
        ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
        ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
        ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
        ("SW1", "Eth0/5"): ("R6", "Eth0/1"),
    }

    return_value = task_11_2.create_network_map(
        ["sh_cdp_n_r2.txt", "sh_cdp_n_r1.txt", "sh_cdp_n_sw1.txt", "sh_cdp_n_r3.txt"]
    )
    assert return_value != None, "The function returns None"
    assert (
        type(return_value) == dict
    ), f"The function should return a dict, instead it returns a {type(return_value).__name__}"
    assert correct_return_value == return_value, "Function returns wrong value"
