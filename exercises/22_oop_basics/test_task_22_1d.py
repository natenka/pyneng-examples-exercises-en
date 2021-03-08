import pytest
import warnings
import task_22_1d
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
    check_class_exists(task_22_1d, "Topology")


def test_attr_topology(topology_with_dupl_links):
    """Checking that the Topology object has a topology attribute"""
    top_with_data = task_22_1d.Topology(topology_with_dupl_links)
    check_attr_or_method(top_with_data, attr="topology")


def test_topology_normalization(topology_with_dupl_links, normalized_topology_example):
    """Checking the removal of duplicates in a topology"""
    top_with_data = task_22_1d.Topology(topology_with_dupl_links)
    assert (
        type(top_with_data.topology) == dict
    ), f"topology attribute should be a dictionary, not a {type(top_with_data.topology).__name__}"
    assert len(top_with_data.topology) == len(
        normalized_topology_example
    ), "After creating an instance, the topology attribute should contain a topology without duplicates"


def test_method_add_link_created(normalized_topology_example):
    norm_top = task_22_1d.Topology(normalized_topology_example)
    check_attr_or_method(norm_top, method="add_link")


def test_method_add_link(normalized_topology_example, capsys):
    norm_top = task_22_1d.Topology(normalized_topology_example)

    add_link_result = norm_top.add_link(("R1", "Eth0/4"), ("R7", "Eth0/0"))
    assert add_link_result == None, "add_link method must return None"

    assert (
        "R1",
        "Eth0/4",
    ) in norm_top.topology, "After adding a connection via the add_link method, it must exist in the topology"
    assert (
        len(norm_top.topology) == 7
    ), "After adding a connection, the number of connections should be 7"

    norm_top.add_link(("R1", "Eth0/4"), ("R7", "Eth0/0"))
    out, err = capsys.readouterr()
    link_msg = "Such a connection already exists"
    assert (
        link_msg in out
    ), "When adding an existing connection, the message 'Such a connection already exists' was not printed"

    norm_top.add_link(("R1", "Eth0/4"), ("R7", "Eth0/5"))
    out, err = capsys.readouterr()
    port_msg = "A link to one of the ports exists"
    assert (
        port_msg in out
    ), "When adding a connection to an existing port, the 'A link to one of the ports exists' message was not printed"
