# -*- coding: utf-8 -*-
"""
Task 4.1

Using the prepared nat string, get a new string where the FastEthernet
interface is replaced with GigabitEthernet.
Print the resulting new string to the standard output (stdout) using print.

Restriction: All tasks must be done using the topics covered in this and previous chapters.

Warning: in section 4, the tests can be easily "tricked" into making the
correct output without getting results from initial data using Python.
This does not mean that the task was done correctly, it is just that at
this stage it is difficult otherwise test the result.
"""

nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
