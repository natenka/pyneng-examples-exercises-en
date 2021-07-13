from functools import wraps
import pytest


# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def test_task(capsys):
    import task_6_3

    out, err = capsys.readouterr()
    correct_stdout = (
        "interface FastEthernet0/1\n"
        " switchport trunk encapsulation dot1q\n"
        " switchport mode trunk\n"
        " switchport trunk allowed vlan add 10,20\n"
        "interface FastEthernet0/2\n"
        " switchport trunk encapsulation dot1q\n"
        " switchport mode trunk\n"
        " switchport trunk allowed vlan 11,30\n"
        "interface FastEthernet0/4\n"
        " switchport trunk encapsulation dot1q\n"
        " switchport mode trunk\n"
        " switchport trunk allowed vlan remove 17\n"
        "interface FastEthernet0/5\n"
        " switchport trunk encapsulation dot1q\n"
        " switchport mode trunk\n"
        " switchport trunk allowed vlan add 10,21\n"
        "interface FastEthernet0/7\n"
        " switchport trunk encapsulation dot1q\n"
        " switchport mode trunk\n"
        " switchport trunk allowed vlan 30"
    )

    assert (
        out
    ), "Nothing is printed to stdout. It is necessary not only to get the correct result, but also to print it to the stdout using print"
    assert correct_stdout == out.strip(), "Wrong output is printed to stdout"
