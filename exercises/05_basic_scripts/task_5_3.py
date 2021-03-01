# -*- coding: utf-8 -*-
"""
Task 5.3

The script should prompt the user for input:
* interface mode (access/trunk)
* interface number (Gi0/3)
* VLAN number (for trunk mode, a list of VLANs will be entered)

Depending on the selected mode, print corresponding access or trunk configuration
on stdout (command templates are in the lists access_template and trunk_template).

The output should first print the interface line and the interface number, and then
the corresponding template in which the VLAN number (or the list of VLANs) is inserted.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
This task can be solved without using the if condition and for/while loops.

Hint:
Leading up to this task was task 5.1. To make it easier to solve this task,
you can look at task 5.1 and figure out exactly how different information
is displayed in the task, depending on user input.

Below are examples of script execution to make it easier to understand the task.

An example of script execution when the access mode is selected:

$ python task_5_3.py
Enter interface mode (access/trunk): access
Enter interface type and number: Fa0/6
Enter VLAN(s) number: 3

interface Fa0/6
switchport mode access
switchport access vlan 3
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable

An example of script execution when the trunk mode is selected:
$ python task_5_3.py
Enter interface mode (access/trunk): trunk
Enter interface type and number: Fa0/7
Enter VLAN(s) number: 2,3,4,5

interface Fa0/7
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan 2,3,4,5
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]
