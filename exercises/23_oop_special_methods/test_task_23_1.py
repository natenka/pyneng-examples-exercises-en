import pytest
import task_23_1
import sys

sys.path.append("..")

from pyneng_common_functions import check_class_exists, check_attr_or_method

# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def test_class_created():
    check_class_exists(task_23_1, "IPAddress")


def test_attr_ipaddress():
    """Verify that the IPAddress object has ip and mask attributes"""
    ip1 = task_23_1.IPAddress("10.1.1.1/24")
    check_attr_or_method(ip1, attr="ip")
    check_attr_or_method(ip1, attr="mask")
    assert ip1.ip == "10.1.1.1", "ip1.ip attribute must be equal to 10.1.1.1"
    assert ip1.mask == 24, "ip1.mask attribute must be equal to 24"


def test_wrong_ip():
    with pytest.raises(ValueError) as excinfo:
        ip1 = task_23_1.IPAddress("10.1.1.1/240")
    with pytest.raises(ValueError) as excinfo:
        ip1 = task_23_1.IPAddress("10.1.400.1/24")
