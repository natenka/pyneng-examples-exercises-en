import pytest

try:
    import task_24_1a
except OSError:
    pytest.fail(
        "For this task, the function MUST be called in the block if __name__ == '__main__':"
    )

from base_connect_class import BaseSSH
from netmiko.ssh_exception import SSHException
import sys

sys.path.append("..")

from pyneng_common_functions import check_class_exists, check_attr_or_method

# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def test_class_created():
    check_class_exists(task_24_1a, "CiscoSSH")


def test_class_inheritance(first_router_from_devices_yaml):
    ssh = task_24_1a.CiscoSSH(**first_router_from_devices_yaml)
    ssh.ssh.disconnect()
    assert isinstance(ssh, BaseSSH), "CiscoSSH class must inherit BaseSSH"
    check_attr_or_method(ssh, method="send_show_command")
    check_attr_or_method(ssh, method="send_cfg_commands")


def test_params_without_password(first_router_from_devices_yaml, monkeypatch):
    params = first_router_from_devices_yaml.copy()
    password = first_router_from_devices_yaml.get("password")
    del params["password"]
    monkeypatch.setattr("builtins.input", lambda x=None: password)
    try:
        ssh = task_24_1a.CiscoSSH(**params)
        ssh.ssh.disconnect()
    except SSHException:
        pytest.fail("Connection error")
