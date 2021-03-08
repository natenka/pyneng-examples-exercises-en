# -*- coding: utf-8 -*-
"""
Task 21.1a

Create parse_output_to_dict function.

Function parameters:
* template is the name of the file containing the TextFSM template.
  For example templates/sh_ip_int_br.template
* command_output - output of the corresponding show command (string)

The function should return a list of dictionaries:
* keys - names of variables in the TextFSM template
* values - parts of the output that correspond to variables

Check the operation of the function on the output of the command
output/sh_ip_int_br.txt and the template templates/sh_ip_int_br.template.
"""
