# -*- coding: utf-8 -*-
"""
Task 4.4

Vlans list is a list of VLANs collected from all devices on the network,
therefore there are duplicate VLAN numbers in the list.

Get a new list of unique VLAN numbers from the vlans list,
sorted in ascending order of numbers. To get the final
list, you cannot delete specific vlans manually.

Write the resulting list to the result variable.
(this is the variable that will be checked in the test)

Print the result list to the standard output (stdout) using print.

Restriction: All tasks must be done using the topics covered in this and previous chapters.

Warning: in section 4, the tests can be easily "tricked" into making the
correct output without getting results from initial data using Python.
This does not mean that the task was done correctly, it is just that at
this stage it is difficult otherwise test the result.
"""

vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
