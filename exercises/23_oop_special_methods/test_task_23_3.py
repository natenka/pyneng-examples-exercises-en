import pytest
import task_23_3
import sys

sys.path.append("..")

from pyneng_common_functions import check_class_exists, check_attr_or_method

# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def test_class_created():
    check_class_exists(task_23_3, "Topology")


def test_attr_topology(topology_with_dupl_links):
    """Checking that the Topology object has a topology attribute"""
    top_with_data = task_23_3.Topology(topology_with_dupl_links)
    check_attr_or_method(top_with_data, attr="topology")


def test_topology_normalization(topology_with_dupl_links, normalized_topology_example):
    """Checking the removal of duplicates in a topology"""
    top_with_data = task_23_3.Topology(topology_with_dupl_links)
    assert len(top_with_data.topology) == len(normalized_topology_example)


def test_method__add__(normalized_topology_example):
    top1 = task_23_3.Topology(normalized_topology_example)
    top1_size_before_add = len(top1.topology)
    top2 = task_23_3.Topology(
        {("R1", "Eth0/4"): ("R7", "Eth0/0"), ("R1", "Eth0/6"): ("R9", "Eth0/0")}
    )
    top2_size_before_add = len(top2.topology)

    check_attr_or_method(top1, method="__add__")
    top3 = top1 + top2
    assert isinstance(
        top3, task_23_3.Topology
    ), "The __add__ method should return a new instance of the Topology class"
    assert len(top3.topology) == 8
    assert (
        len(top1.topology) == top1_size_before_add
    ), "After the addition, the size of the first topology changed. The __add__ method should not change the original topologies"
    assert (
        len(top2.topology) == top2_size_before_add
    ), "After the addition, the size of the second topology changed. The __add__ method should not change the original topologies"
