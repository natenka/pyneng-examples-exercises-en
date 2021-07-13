import pytest
import task_22_1a
import sys

sys.path.append("..")

from pyneng_common_functions import (
    check_class_exists,
    check_attr_or_method,
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
    check_class_exists(task_22_1a, "Topology")


def test_attr_topology(topology_with_dupl_links):
    """Checking that the Topology object has a topology attribute"""
    top_with_data = task_22_1a.Topology(topology_with_dupl_links)
    check_attr_or_method(top_with_data, attr="topology")


def test_method_normalize(topology_with_dupl_links):
    """Checking that the Topology object has method _normalize"""
    top_with_data = task_22_1a.Topology(topology_with_dupl_links)
    check_attr_or_method(top_with_data, method="_normalize")


def test_topology_normalization(topology_with_dupl_links, normalized_topology_example):
    """Checking the removal of duplicates in a topology"""
    correct_topology = unify_topology_dict(normalized_topology_example)
    return_value = task_22_1a.Topology(topology_with_dupl_links)
    return_topology = unify_topology_dict(return_value.topology)
    assert (
        type(return_value.topology) == dict
    ), f"topology attribute should be a dictionary, not a {type(top_with_data.topology).__name__}"
    assert len(correct_topology) == len(
        return_value.topology
    ), "After creating an instance, the topology attribute should contain a topology without duplicates"
    assert (
        correct_topology == return_topology
    ), "After creating an instance, the topology attribute should contain a topology without duplicates"
