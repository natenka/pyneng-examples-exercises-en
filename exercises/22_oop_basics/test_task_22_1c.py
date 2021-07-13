import pytest
import warnings
import task_22_1c
import sys

sys.path.append("..")

from pyneng_common_functions import (
    check_class_exists,
    check_attr_or_method,
    stdout_incorrect_warning,
    unify_topology_dict,
)

# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def test_class_created():
    """
    Checking that the class has been created
    """
    check_class_exists(task_22_1c, "Topology")


def test_attr_topology(topology_with_dupl_links):
    """Checking that the Topology object has a topology attribute"""
    top_with_data = task_22_1c.Topology(topology_with_dupl_links)
    check_attr_or_method(top_with_data, attr="topology")


def test_topology_normalization(topology_with_dupl_links, normalized_topology_example):
    """Checking the removal of duplicates in a topology"""
    top_with_data = task_22_1c.Topology(topology_with_dupl_links)
    assert (
        type(top_with_data.topology) == dict
    ), f"topology attribute should be a dictionary, not a {type(top_with_data.topology).__name__}"
    assert len(top_with_data.topology) == len(
        normalized_topology_example
    ), "After creating an instance, the topology attribute should contain a topology without duplicates"
    correct_topology = unify_topology_dict(normalized_topology_example)
    return_value = task_22_1c.Topology(topology_with_dupl_links)
    return_topology = unify_topology_dict(return_value.topology)
    assert (
        type(return_value.topology) == dict
    ), f"topology attribute should be a dictionary, not a {type(top_with_data.topology).__name__}"
    assert len(correct_topology) == len(
        return_value.topology
    ), "After creating an instance, the topology attribute should contain a topology without duplicates"


def test_method_delete_node_created(
    topology_with_dupl_links, normalized_topology_example
):
    return_value = task_22_1c.Topology(normalized_topology_example)
    check_attr_or_method(return_value, method="delete_node")


def test_method_delete_node(normalized_topology_example, capsys):
    return_value = task_22_1c.Topology(normalized_topology_example)

    node = "SW1"
    delete_node_result = return_value.delete_node(node)
    assert None == delete_node_result, "The delete_node method should return None"

    ports_with_node = [
        src for src, dst in return_value.topology.items() if node in src or node in dst
    ]
    assert 0 == len(ports_with_node), "Links to host SW1 have not been deleted"
    assert 3 == len(
        return_value.topology
    ), "Only three connections should remain in the topology"

    return_value.delete_node(node)
    stdout, err = capsys.readouterr()
    assert (
        "There is no such device" in stdout
    ), "When deleting a non-existent device, the message 'There is no such device' was not displayed"
