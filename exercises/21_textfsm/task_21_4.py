# -*- coding: utf-8 -*-
"""
Task 21.4

Create function send_and_parse_show_command.

Function parameters:
* device_dict - a dict with connectin parameters for one device
* command - the command to be executed
* templates_path - path to the directory with TextFSM templates
* index - file index name, default value "index"

The function should connect to one device, send a show command using netmiko,
and then parse the command output using TextFSM.

The function should return a list of dictionaries with the results
of parsing the command output (as in task 21.1a):
* keys - names of variables in the TextFSM template
* values - parts of the output that correspond to variables

Check the operation of the function using the output
of the sh ip int br command and devices from devices.yaml.

"""
