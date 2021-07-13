import pytest
import task_21_1
import os
import sys

sys.path.append("..")

from pyneng_common_functions import get_textfsm_output


# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def test_templates_exists():
    """
    Checking that the function has been created
    """
    assert os.path.exists(
        "templates/sh_ip_dhcp_snooping.template"
    ), "Template templates/sh_ip_dhcp_snooping.template does not exist"


def test_template():
    correct_return_value = [
        ["mac", "ip", "vlan", "intf"],
        ["00:09:BB:3D:D6:58", "10.1.10.2", "10", "FastEthernet0/1"],
        ["00:04:A3:3E:5B:69", "10.1.5.2", "5", "FastEthernet0/10"],
        ["00:05:B3:7E:9B:60", "10.1.5.4", "5", "FastEthernet0/9"],
        ["00:09:BC:3F:A6:50", "10.1.10.6", "10", "FastEthernet0/3"],
    ]
    with open("output/sh_ip_dhcp_snooping.txt") as show:
        sh_ip_dhcp_snoop = show.read()
    template = "templates/sh_ip_dhcp_snooping.template"
    return_value = get_textfsm_output(template, sh_ip_dhcp_snoop)

    assert (
        correct_return_value == return_value
    ), "Template templates/sh_ip_dhcp_snooping.template does not parse data correctly"
