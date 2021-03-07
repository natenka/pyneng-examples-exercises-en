# -*- coding: utf-8 -*-
"""
Task 9.4

Create a convert_config_to_dict function that handles the switch configuration
file and returns a dictionary:
* All top-level commands (global configuration mode) will be keys.
* If the top-level team has subcommands, they must be in the value
  from the corresponding key, in the form of a list (spaces at the beginning of the line must be removed).
* If the top-level command has no subcommands, then the value will be an empty list

The function must have one parameter, config_filename, which expects as an argument
the name of the configuration file.

Check the operation of the function using the config_sw1.txt file.

When processing the configuration file, you should ignore the lines that begin
with '!', as well as lines containing words from the ignore list.

To check if a line should be ignored, use the ignore_command function.

The part of the dictionary that the function should return (the full output can be seen
in test_task_9_4.py test):
{
    "version 15.0": [],
    "service timestamps debug datetime msec": [],
    "service timestamps log datetime msec": [],
    "no service password-encryption": [],
    "hostname sw1": [],
    "interface FastEthernet0/0": [
        "switchport mode access",
        "switchport access vlan 10",
    ],
    "interface FastEthernet0/1": [
        "switchport trunk encapsulation dot1q",
        "switchport trunk allowed vlan 100,200",
        "switchport mode trunk",
    ],
    "interface FastEthernet0/2": [
        "switchport mode access",
        "switchport access vlan 20",
    ],
}

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""

ignore = ["duplex", "alias", "configuration"]


def ignore_command(command, ignore):
    """
    The function checks if the command contains a word from the ignore list.

    command is a string. Command to check
    ignore is a list. Word list

    Returns
    * True if the command contains a word from the ignore list
    * False - if not
    """
    ignore_status = False
    for word in ignore:
        if word in command:
            ignore_status = True
    return ignore_status
