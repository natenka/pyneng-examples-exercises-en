# -*- coding: utf-8 -*-
"""
Task 21.2

Create a TextFSM template to parse the output of the sh ip dhcp snooping binding
command and write it to templates/sh_ip_dhcp_snooping.template

The command output is located in the file output/sh_ip_dhcp_snooping.txt.

The template should process and return the values of such columns:
* mac - 00:04:A3:3E:5B:69
* ip - 10.1.10.6
* vlan - 10
* intf - FastEthernet0/10

Check the work of the template using the parse_command_output function
from task 21.1.
"""
