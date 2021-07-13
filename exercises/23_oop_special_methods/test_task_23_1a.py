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
    return_ip = task_23_1a.IPAddress("10.1.1.1/24")
    check_attr_or_method(return_ip, attr="ip")
    check_attr_or_method(return_ip, attr="mask")
    assert (
        "10.1.1.1" == return_ip.ip
    ), "return_ip.ip attribute must be equal to 10.1.1.1"
    assert 24 == return_ip.mask, "return_ip.mask attribute must be equal to 24"


def test_str_method():
    return_ip = task_23_1a.IPAddress("10.5.5.5/24")
    assert "IP address 10.5.5.5/24" == str(
        return_ip
    ), "The __str__ method should return 'IP address 10.5.5.5/24'"


def test_repr_method():
    return_ip = task_23_1a.IPAddress("10.5.5.5/24")
    assert "IPAddress('10.5.5.5/24')" == repr(return_ip).replace(
        '"', "'"
    ), "The __str__ method should return IPAddress('10.5.5.5/24')"
