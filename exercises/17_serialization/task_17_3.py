# -*- coding: utf-8 -*-
"""
Task 17.3

Create a function parse_sh_cdp_neighbors that processes the output of
the show cdp neighbors command.

The function expects, as an argument, the output of the command
as a single string (not a filename).
The function should return a dictionary that describes the connections between devices.

For example, if the following output was passed as an argument:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

The function should return a dictionary like this:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Interfaces must be written with a space. That is, so Fa 0/0, and not so Fa0/0.


Check the function on the contents of the sh_cdp_n_sw1.txt file
"""
