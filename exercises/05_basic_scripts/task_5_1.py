# -*- coding: utf-8 -*-
"""
Task 5.1

The task contains a dictionary with information about different devices.

In the task you need: ask the user to enter the device name (r1, r2 or sw1).
Print information about the corresponding device to standard output
(information will be in the form of a dictionary).

An example of script execution:
$ python task_5_1.py
Enter device name: r1
{'location': '21 New Globe Walk', 'vendor': 'Cisco', 'model': '4451', 'ios': '15.4', 'ip': '10.255.0.1'}

Restriction: You cannot modify the london_co dictionary.

All tasks must be completed using only the topics covered. That is, this task can be
solved without using the if condition.
"""

london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1",
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    },
}
