import pytest
import warnings
import task_22_1d
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
    check_class_exists(task_22_1d, "Topology")


def test_attr_topology(topology_with_dupl_links):
    """Checking that the Topology object has a topology attribute"""
    return_value = task_22_1d.Topology(topology_with_dupl_links)
    check_attr_or_method(return_value, attr="topology")


def test_topology_normalization(topology_with_dupl_links, normalized_topology_example):
    """Checking the removal of duplicates in a topology"""
    correct_topology = unify_topology_dict(normalized_topology_example)
    return_value = task_22_1d.Topology(topology_with_dupl_links)
    assert (
        type(return_value.topology) == dict
    ), f"topology attribute should be a dictionary, not a {type(top_with_data.topology).__name__}"
    assert len(correct_topology) == len(
        return_value.topology
    ), "After creating an instance, the topology attribute should contain a topology without duplicates"


def test_method_add_link_created(normalized_topology_example):
    return_value = task_22_1d.Topology(normalized_topology_example)
    check_attr_or_method(return_value, method="add_link")


def test_method_add_link(normalized_topology_example, capsys):
    return_value = task_22_1d.Topology(normalized_topology_example)

    add_link_result = return_value.add_link(("R1", "Eth0/4"), ("R7", "Eth0/0"))
    assert None == add_link_result, "add_link method must return None"

    assert (
        "R1",
        "Eth0/4",
    ) in return_value.topology, "After adding a connection via the add_link method, it must exist in the topology"
    assert 7 == len(
        return_value.topology
    ), "After adding a connection, the number of connections should be 7"

    return_value.add_link(("R1", "Eth0/4"), ("R7", "Eth0/0"))
    stdout, err = capsys.readouterr()
    assert (
        "Such a connection already exists" in stdout
    ), "When adding an existing connection, the message 'Such a connection already exists' was not printed"

    return_value.add_link(("R1", "Eth0/4"), ("R7", "Eth0/5"))
    stdout, err = capsys.readouterr()
    assert (
        "A link to one of the ports exists" in stdout
    ), "When adding a connection to an existing port, the 'A link to one of the ports exists' message was not printed"
