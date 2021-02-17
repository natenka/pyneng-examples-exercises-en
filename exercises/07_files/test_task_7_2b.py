from functools import wraps
import pytest

# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def test_task(monkeypatch, tmpdir):
    dest_filename = tmpdir.mkdir("test_tasks").join("task_7_2b.txt")

    monkeypatch.setattr("sys.argv", ["task_7_2b.py", "config_sw1.txt", dest_filename])
    import task_7_2b
    dest_file_content = dest_filename.read().strip()

    correct_file_content = (
        "version 15.0\n"
        "service timestamps debug datetime msec\n"
        "service timestamps log datetime msec\n"
        "no service password-encryption\n"
        "hostname sw1\n"
        "interface Ethernet0/0\n"
        "interface Ethernet0/1\n"
        " switchport trunk encapsulation dot1q\n"
        " switchport trunk allowed vlan 100\n"
        " switchport mode trunk\n"
        " spanning-tree portfast edge trunk\n"
        "interface Ethernet0/2\n"
        "interface Ethernet0/3\n"
        " switchport trunk encapsulation dot1q\n"
        " switchport trunk allowed vlan 100\n"
        " switchport mode trunk\n"
        " spanning-tree portfast edge trunk\n"
        "interface Ethernet1/0\n"
        "interface Ethernet1/1\n"
        "interface Ethernet1/2\n"
        "interface Ethernet1/3\n"
        "interface Vlan100\n"
        " ip address 10.0.100.1 255.255.255.0\n"
        "line con 0\n"
        " exec-timeout 0 0\n"
        " privilege level 15\n"
        " logging synchronous\n"
        "line aux 0\n"
        "line vty 0 4\n"
        " login\n"
        " transport input all\n"
        "end"
    )

    assert (
        dest_file_content == correct_file_content
    ), "Wrong output is printed to stdout"

