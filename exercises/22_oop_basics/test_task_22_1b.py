import pytest
import warnings
import task_22_1b
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
    check_class_exists(task_22_1b, "Topology")


def test_attr_topology(topology_with_dupl_links):
    """Checking that the Topology object has a topology attribute"""
    top_with_data = task_22_1b.Topology(topology_with_dupl_links)
    check_attr_or_method(top_with_data, attr="topology")


def test_topology_normalization(topology_with_dupl_links, normalized_topology_example):
    """Checking the removal of duplicates in a topology"""
    top_with_data = task_22_1b.Topology(topology_with_dupl_links)
    assert (
        type(top_with_data.topology) == dict
    ), f"topology attribute should be a dictionary, not a {type(top_with_data.topology).__name__}"
    assert len(top_with_data.topology) == len(
        normalized_topology_example
    ), "After creating an instance, the topology attribute should contain a topology without duplicates"


def test_method_delete_link_created(
    topology_with_dupl_links, normalized_topology_example
):
    norm_top = task_22_1b.Topology(normalized_topology_example)
    check_attr_or_method(norm_top, method="delete_link")


def test_method_delete_link(normalized_topology_example, capsys):
    norm_top = task_22_1b.Topology(normalized_topology_example)
    delete_link_result = norm_top.delete_link(("R3", "Eth0/0"), ("SW1", "Eth0/3"))
    assert delete_link_result == None, "The delete_link method should return None"

    assert ("R3", "Eth0/0") not in norm_top.topology, "The link was not deleted"

    norm_top.delete_link(("R5", "Eth0/0"), ("R3", "Eth0/2"))
    assert ("R3", "Eth0/2") not in norm_top.topology, "The link was not deleted"

    norm_top.delete_link(("R8", "Eth0/2"), ("R9", "Eth0/1"))
    out, err = capsys.readouterr()
    link_msg = "There is no such link"
    assert (
        link_msg in out
    ), "When deleting a nonexistent connection, the message 'There is no such link' was not printed"
