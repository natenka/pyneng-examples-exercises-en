# -*- coding: utf-8 -*-

"""
Task 23.2

Copy the CiscoTelnet class from task 22.2 and add context manager
support to the class. When exiting the context manager block, the connection
should be closed.

Example of work:

In [14]: r1_params = {
    ...:     'ip': '192.168.100.1',
    ...:     'username': 'cisco',
    ...:     'password': 'cisco',
    ...:     'secret': 'cisco'}

In [15]: from task_23_2 import CiscoTelnet

In [16]: with CiscoTelnet(**r1_params) as r1:
    ...:     print(r1.send_show_command('sh clock'))
    ...:
sh clock
*19:17:20.244 UTC Sat Apr 6 2019
R1#

The test checks the connection with parameters from the devices.yaml file.
The file must contain the parameters of the available devices.
"""
