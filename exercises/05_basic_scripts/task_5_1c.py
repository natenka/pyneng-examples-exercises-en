# -*- coding: utf-8 -*-
"""
Task 5.1c

Copy and modify the script from task 5.1b so that when you request a parameter
that is not in the device dictionary, the message 'There is no such parameter' is displayed.
The assignment applies only to the parameters of the devices, not to the devices themselves.

> Try typing a non-existent parameter, to see what the result will be. And then complete the task.

If an existing parameter is selected, print information about the corresponding parameter.

An example of script execution:
$ python task_5_1c.py
Enter device name: r1
Enter parameter name (ios, model, vendor, location, ip): ips
There is no such parameter

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
