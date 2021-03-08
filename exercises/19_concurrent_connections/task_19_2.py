# -*- coding: utf-8 -*-
"""
Task 19.2

Create a send_show_command_to_devices function that sends the same show command
to different devices in concurrent threads and then writes the output of
the commands to a file. The output from the devices in the file can be in any order.

Function parameters:
* devices - a list of dictionaries with parameters for connecting to devices
* command - show command
* filename - is the name of a text file to which the output of all commands will be written
* limit - maximum number of concurrent threads (default 3)

The function returns None.

The output of the commands should be written to a plain text file in this
format (before the output of the command, you must write the hostname and
the command itself):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.2   YES NVRAM  up                    up
Ethernet0/1                10.1.1.1        YES NVRAM  administratively down down
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down

You can create any additional functions to complete the task.

Check the operation of the function on devices from the devices.yaml file.
"""
