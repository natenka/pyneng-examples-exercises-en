import os
import yaml
import pytest
import task_17_3b
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists, unify_topology_dict

# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def test_function_created():
    """
    Checking that the function has been created
    """
    check_function_exists(task_17_3b, "transform_topology")


def test_function_return_value():
    """
    Function check
    """
    sh_cdp_topology_tuples = {
        ("R1", "Eth 0/0"): ("SW1", "Eth 0/1"),
        ("R2", "Eth 0/0"): ("SW1", "Eth 0/2"),
        ("R2", "Eth 0/1"): ("R5", "Eth 0/0"),
        ("R2", "Eth 0/2"): ("R6", "Eth 0/1"),
        ("R3", "Eth 0/0"): ("SW1", "Eth 0/3"),
        ("R4", "Eth 0/0"): ("SW1", "Eth 0/4"),
        ("R4", "Eth 0/1"): ("R5", "Eth 0/1"),
    }
    correct_return_value = unify_topology_dict(sh_cdp_topology_tuples)

    assert os.path.exists("topology.yaml"), "topology.yaml file does not exist"
    return_value = task_17_3b.transform_topology("topology.yaml")
    assert return_value != None, "The function returns None"
    assert (
        type(return_value) == dict
    ), f"The function should return a dict, instead it returns a {type(return_value).__name__}"
    assert (
        unify_topology_dict(return_value) == correct_return_value
    ), "Function returns wrong value"
