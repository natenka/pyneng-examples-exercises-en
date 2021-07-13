import pytest
import task_12_1
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists, ping, get_reach_unreach

# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def test_function_created():
    """
    Checking that the function has been created
    """
    check_function_exists(task_12_1, "ping_ip_addresses")


@pytest.mark.skipif(
    not hasattr(task_12_1, "ping_ip_addresses"),
    reason="This test only works if a function ping_ip_addresses is created",
)
def test_function_return_value():
    """
    Function check
    """
    list_of_ips = ["1.1.1", "8.8.8.8", "8.8.4.4", "8.8.7.1"]
    correct_return_value = get_reach_unreach(list_of_ips)

    return_value = task_12_1.ping_ip_addresses(list_of_ips)
    assert return_value != None, "The function returns None"
    assert type(return_value) == tuple and all(
        type(item) == list for item in return_value
    ), "The function must return a tuple with two lists"
    assert correct_return_value == return_value, "Function returns wrong value"
