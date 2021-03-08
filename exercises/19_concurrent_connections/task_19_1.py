# -*- coding: utf-8 -*-
"""
Task 19.1

Create a ping_ip_addresses function that checks if IP addresses are pingable.
Checking IP addresses should be done concurrent in different threads.

Ping_ip_addresses function parameters:
* ip_list - list of IP addresses
* limit - maximum number of parallel threads (default 3)

The function must return a tuple with two lists:
* list of available IP addresses
* list of unavailable IP addresses

You can create any additional functions to complete the task.

To check the availability of an IP address, use ping.

A hint about working with concurrent.futures:
If you need to ping several IP addresses in different threads, you need to create
a function that will ping one IP address, and then run this function in different
threads for different IP addresses using concurrent.futures (this last part
must be done in the ping_ip_addresses function).

"""
