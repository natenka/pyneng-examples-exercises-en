# -*- coding: utf-8 -*-
"""
Task 21.3

Create function parse_command_dynamic.

Function parameters:
* command_output - command output (string)
* attributes_dict - an attribute dict containing the following key-value pairs:
 * 'Command': command
 * 'Vendor': vendor
* index_file is the name of the file where the correspondence between commands
  and templates is stored. The default is "index"
* templ_path - directory where templates are stored. The default is "templates"

The function should return a list of dicts with the results
of parsing the command output (as in task 21.1a):
* keys - names of variables in the TextFSM template
* values - parts of the output that correspond to variables

Check the function on the output of the sh ip int br command.
"""
