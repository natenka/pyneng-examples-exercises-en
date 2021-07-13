import pytest
import task_19_3a
import yaml
import sys

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
    check_function_exists(task_19_3a, "send_command_to_devices")


@pytest.mark.parametrize(
    "device,command_dict",
    [
        (r1, {r1["host"]: ["sh version | include IOS", "sh int desc"]}),
        (r2, {r2["host"]: ["sh ip int br", "sh run | s ^router ospf"]}),
        (r3, {r3["host"]: ["sh int desc"]}),
    ],
)
def test_function_return_value_from_single_device(
    three_routers_from_devices_yaml,
    r1_r2_r3_test_connection,
    tmpdir,
    device,
    command_dict,
):
    """
    Function check
    """
    device_ip = device["host"]
    commands = command_dict[device_ip]
    ssh = create_ssh_connect(device)
    output = ""
    for command in commands:
        output += f"{ssh.find_prompt()}{command}\n{ssh.send_command(command)}\n"
    ssh.disconnect()
    correct_output = strip_empty_lines(output)
    dest_filename = tmpdir.mkdir("test_tasks").join("task_19_3.txt")

    return_value = task_19_3a.send_command_to_devices(
        devices=[device],
        commands_dict=command_dict,
        filename=dest_filename,
        limit=3,
    )
    assert None == return_value, "The function must return None"
    dest_file_content = strip_empty_lines(dest_filename.read().strip())

    assert (
        correct_output == dest_file_content
    ), f"Output file does not have output from {device_ip}"


def test_function_return_value_from_all_devices(
    three_routers_from_devices_yaml, r1_r2_r3_test_connection, tmpdir
):
    """
    Function check
    """
    routers_ip = [router["host"] for router in three_routers_from_devices_yaml]
    command = "sh ip int br"
    out1, out2, out3 = [r.send_command(command) for r in r1_r2_r3_test_connection]
    dest_filename = tmpdir.mkdir("test_tasks").join("task_19_3.txt")

    return_value = task_19_3a.send_command_to_devices(
        three_routers_from_devices_yaml,
        dict(zip(routers_ip, [[command]] * 3)),
        dest_filename,
        limit=3,
    )
    assert None == return_value, "The function must return None"

    dest_file_content = dest_filename.read().strip()

    assert (
        out1.strip() in dest_file_content
    ), "Output file does not have output from first device"
    assert (
        out2.strip() in dest_file_content
    ), "Output file does not have output fromо second device"
    assert (
        out3.strip() in dest_file_content
    ), "Output file does not have output from third device"
