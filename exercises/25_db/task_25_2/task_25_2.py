# -*- coding: utf-8 -*-
'''
Task 25.2

There are no tests for the tasks of the 25th chapter!

In this task, you need to create the get_data.py script.

The code in the script should be broken down into functions.
It is up to you to decide which functions and how to split the code.
Some of the code can be global.

The script can be passed arguments and, depending on the arguments,
you need to display different information.
If the script is called:
* with no arguments, print the entire contents of the dhcp table
* with two arguments, display information from the dhcp table that matches
  the field and value
* with any other number of arguments, print a message that the script
  only supports two or zero arguments

The database file can be copied from task 25.1.

Examples of output for different numbers and values of arguments:

$ python get_data.py
The dhcp table has the following entries:
-----------------  ---------------  --  ----------------  ---
00:09:BB:3D:D6:58  10.1.10.2        10  FastEthernet0/1   sw1
00:04:A3:3E:5B:69  10.1.5.2          5  FastEthernet0/10  sw1
00:05:B3:7E:9B:60  10.1.5.4          5  FastEthernet0/9   sw1
00:07:BC:3F:A6:50  10.1.10.6        10  FastEthernet0/3   sw1
00:09:BC:3F:A6:50  192.168.100.100   1  FastEthernet0/7   sw1
00:E9:BC:3F:A6:50  100.1.1.6         3  FastEthernet0/20  sw3
00:E9:22:11:A6:50  100.1.1.7         3  FastEthernet0/21  sw3
00:A9:BB:3D:D6:58  10.1.10.20       10  FastEthernet0/7   sw2
00:B4:A3:3E:5B:69  10.1.5.20         5  FastEthernet0/5   sw2
00:C5:B3:7E:9B:60  10.1.5.40         5  FastEthernet0/9   sw2
00:A9:BC:3F:A6:50  10.1.10.60       20  FastEthernet0/2   sw2
-----------------  ---------------  --  ----------------  ---

$ python get_data.py vlan 10

Information about devices with the following parameters: vlan 10
-----------------  ----------  --  ---------------  ---
00:09:BB:3D:D6:58  10.1.10.2   10  FastEthernet0/1  sw1
00:07:BC:3F:A6:50  10.1.10.6   10  FastEthernet0/3  sw1
00:A9:BB:3D:D6:58  10.1.10.20  10  FastEthernet0/7  sw2
-----------------  ----------  --  ---------------  ---

$ python get_data.py ip 10.1.10.2

Information about devices with the following parameters: ip 10.1.10.2
-----------------  ---------  --  ---------------  ---
00:09:BB:3D:D6:58  10.1.10.2  10  FastEthernet0/1  sw1
-----------------  ---------  --  ---------------  ---

$ python get_data.py vln 10
This parameter is not supported.
Valid parameter values: mac, ip, vlan, interface, switch

$ python get_data.py ip vlan 10
Please enter two or zero arguments

'''
