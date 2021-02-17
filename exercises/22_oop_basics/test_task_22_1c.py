import pytest
import warnings
import task_22_1c
import sys

sys.path.append("..")

from pyneng_common_functions import (
    check_class_exists,
    check_attr_or_method,
    stdout_incorrect_warning,
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


def test_method_delete_node_created(
    topology_with_dupl_links, normalized_topology_example
):
    norm_top = task_22_1c.Topology(normalized_topology_example)
    check_attr_or_method(norm_top, method="delete_node")


def test_method_delete_node(normalized_topology_example, capsys):
    norm_top = task_22_1c.Topology(normalized_topology_example)

    node = "SW1"
    delete_node_result = norm_top.delete_node(node)
    assert delete_node_result == None, "The delete_node method should return None"

    ports_with_node = [
        src for src, dst in norm_top.topology.items() if node in src or node in dst
    ]
    assert len(ports_with_node) == 0, "Links to host SW1 have not been deleted"
    assert (
        len(norm_top.topology) == 3
    ), "Only three connections should remain in the topology"

    norm_top.delete_node(node)
    out, err = capsys.readouterr()
    node_msg = "There is no such device"
    assert (
        node_msg in out
    ), "When deleting a non-existent device, the message 'There is no such device' was not displayed"
