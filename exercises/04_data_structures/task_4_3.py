# -*- coding: utf-8 -*-
"""
Task 4.3

Get the following list of VLANs from the config string:
['1', '3', '10', '20', '30', '100']

Write the resulting list to the result variable.
(this is the variable that will be checked in the test)

Print the result list to the standard output (stdout) using print.

Here is a very important point that you need to get exactly the list (data type),
and not, for example, a string that looks like the list shown.

Restriction: All tasks must be done using the topics covered in this and previous chapters.

Warning: in section 4, the tests can be easily "tricked" into making the
correct output without getting results from initial data using Python.
This does not mean that the task was done correctly, it is just that at
this stage it is difficult otherwise test the result.
"""

config = "switchport trunk allowed vlan 1,3,10,20,30,100"
