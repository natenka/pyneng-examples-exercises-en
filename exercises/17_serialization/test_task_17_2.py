import pytest
import task_17_2
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists, read_all_csv_content_as_list

# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def test_functions_created():
    """
    Checking that the functions has been created
    """
    check_function_exists(task_17_2, "parse_sh_version")
    check_function_exists(task_17_2, "write_inventory_to_csv")


def test_parse_sh_version_return_value():
    """
    Function check
    """
    with open("sh_version_r1.txt") as f:
        sh_version_r1 = f.read()
    with open("sh_version_r2.txt") as f:
        sh_version_r2 = f.read()

    correct_return_value_r1 = (
        "12.4(15)T1",
        "flash:c1841-advipservicesk9-mz.124-15.T1.bin",
        "15 days, 8 hours, 32 minutes",
    )
    correct_return_value_r2 = (
        "12.4(4)T",
        "disk0:c7200-js-mz.124-4.T",
        "45 days, 8 hours, 22 minutes",
    )

    return_value_r1 = task_17_2.parse_sh_version(sh_version_r1)
    assert return_value_r1 != None, "The function returns None"
    assert (
        type(return_value_r1) == tuple
    ), f"The function should return a tuple, instead it returns a {type(return_value_r1).__name__}"
    assert (
        return_value_r1 == correct_return_value_r1
    ), "Function returns wrong value for r1"
    return_value_r2 = task_17_2.parse_sh_version(sh_version_r2)
    assert (
        return_value_r2 == correct_return_value_r2
    ), "Function returns wrong value for r2"


def test_write_to_csv_return_value(tmpdir):
    """
    Function check
    """
    routers_inventory = [
        ["hostname", "ios", "image", "uptime"],
        [
            "r1",
            "12.4(15)T1",
            "flash:c1841-advipservicesk9-mz.124-15.T1.bin",
            "15 days, 8 hours, 32 minutes",
        ],
        ["r2", "12.4(4)T", "disk0:c7200-js-mz.124-4.T", "45 days, 8 hours, 22 minutes"],
        ["r3", "12.4(4)T", "disk0:c7200-js-mz.124-4.T", "5 days, 18 hours, 2 minutes"],
    ]
    sh_version_files = ["sh_version_r1.txt", "sh_version_r2.txt", "sh_version_r3.txt"]
    dest_filename = tmpdir.mkdir("test_tasks").join("routers_inventory.csv")
    return_value = task_17_2.write_inventory_to_csv(sh_version_files, dest_filename)
    csv_content = read_all_csv_content_as_list(dest_filename)
    correct_return_value = sorted(routers_inventory)

    assert (
        return_value == None
    ), f"The function must return None, and it returns a {type(return_value).__name__}"
    assert (
        sorted(csv_content) == correct_return_value
    ), "Function returns wrong value"
