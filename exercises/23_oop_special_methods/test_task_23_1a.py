import pytest
import task_23_1a
import sys

sys.path.append("..")

from pyneng_common_functions import check_class_exists, check_attr_or_method

# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def test_class_created():
    check_class_exists(task_23_1a, "IPAddress")


def test_attr_ipaddress():
    ip1 = task_23_1a.IPAddress("10.1.1.1/24")
    check_attr_or_method(ip1, attr="ip")
    check_attr_or_method(ip1, attr="mask")
    assert ip1.ip == "10.1.1.1", "ip1.ip attribute must be equal to 10.1.1.1"
    assert ip1.mask == 24, "ip1.mask attribute must be equal to 24"


def test_str_method():
    ip1 = task_23_1a.IPAddress("10.5.5.5/24")
    assert (
        str(ip1) == "IP address 10.5.5.5/24"
    ), "The __str__ method should return 'IP address 10.5.5.5/24'"


def test_repr_method():
    ip1 = task_23_1a.IPAddress("10.5.5.5/24")
    assert (
        repr(ip1) == "IPAddress('10.5.5.5/24')"
    ), "The __str__ method should return IPAddress('10.5.5.5/24')"
