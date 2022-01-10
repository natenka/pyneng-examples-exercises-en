# -*- coding: utf-8 -*-
"""
Task 12.1

Create a ping_ip_addresses function that checks if IP addresses are pingable.

The function expects a list of IP addresses as an argument.

The function must return a tuple with two lists:
* list of reachable IP addresses
* list of unreachable IP addresses

To check if an IP address is reachable, use the ping command (use subprocess).
The IP address is considered reachable if the execution of the ping command
completed with return code 0.
Nuances: on Windows, the return code can be 0 not only when ping was successful,
but it is the code that needs to be checked for the job. This is to simplify tests.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
