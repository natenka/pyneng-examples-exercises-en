# -*- coding: utf-8 -*-
"""
Task 18.2a


Copy the send_config_commands function from job 18.2 and add the log parameter.
The log parameter controls whether information is displayed about which device
the connection is to:
* if log is equal to True - information is printed
* if log is equal to False - information is not printed

By default, log is equal to True.

An example of how the function works:

In [13]: result = send_config_commands(r1, commands)
Connecting to 192.168.100.1...

In [14]: result = send_config_commands(r1, commands, log=False)

In [15]:

The script should send command command to all devices from the devices.yaml file
using the send_config_commands function.
"""
