import pytest
import task_19_2
import sys
import yaml

sys.path.append("..")

from pyneng_common_functions import (
    check_function_exists,
    strip_empty_lines,
)

from conftest import create_ssh_connect

# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


with open("devices.yaml") as f:
    devices = yaml.safe_load(f)
    devices = devices[:3]
    r1, r2, r3 = devices


def test_functions_created():
    """
    Checking that the function has been created
    """
    check_function_exists(task_19_2, "send_show_command_to_devices")


@pytest.mark.parametrize(
    "device,command",
    [(r1, "sh ip int br | include up +up"), (r2, "sh ip int br"), (r3, "sh int desc")],
)
def test_function_return_value_from_single_device(
    three_routers_from_devices_yaml, r1_r2_r3_test_connection, tmpdir, device, command
):
    """
    Function check
    """
    ssh = create_ssh_connect(device)
    correct_output = strip_empty_lines(
        f"{ssh.find_prompt()}{command}\n{ssh.send_command(command)}\n"
    )
    ssh.disconnect()
    dest_filename = tmpdir.mkdir("test_tasks").join("task_19_2.txt")

    return_value = task_19_2.send_show_command_to_devices(
        devices=[device],
        command=command,
        filename=dest_filename,
        limit=3,
    )
    assert None == return_value, "The function must return None"
    dest_file_content = strip_empty_lines(dest_filename.read().strip())

    assert (
        correct_output == dest_file_content
    ), f"Output file does not have output from {device['host']}"


def test_function_return_value_from_all_devices(
    three_routers_from_devices_yaml, r1_r2_r3_test_connection, tmpdir
):
    command = "sh ip int br"
    out1, out2, out3 = [r.send_command(command) for r in r1_r2_r3_test_connection]
    dest_filename = tmpdir.mkdir("test_tasks").join("task_19_2.txt")

    return_value = task_19_2.send_show_command_to_devices(
        devices=three_routers_from_devices_yaml,
        command=command,
        filename=dest_filename,
        limit=3,
    )
    assert None == return_value, "The function must return None"

    dest_file_content = dest_filename.read().strip()

    assert (
        out1.strip() in dest_file_content
    ), "Output file does not have output from first device"
    assert (
        out2.strip() in dest_file_content
    ), "Output file does not have output from second device"
    assert (
        out3.strip() in dest_file_content
    ), "Output file does not have output from third device"
