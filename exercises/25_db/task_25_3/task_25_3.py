# -*- coding: utf-8 -*-
"""
Task 25.3

There are no tests for the tasks of the 25th chapter!

In previous tasks, information was added to an empty database.
In this task, the script should work correctly even in a situation where
the database already contains information.

Copy the add_data.py script from task 25.1 and try running it again
on the existing database. The output should be like this:

$ python add_data.py
Adding data to the switches table...
While adding data: ('sw1', 'London, 21 New Globe Walk') An error occurred: UNIQUE constraint failed: switches.hostname
While adding data: ('sw2', 'London, 21 New Globe Walk') An error occurred: UNIQUE constraint failed: switches.hostname
While adding data: ('sw3', 'London, 21 New Globe Walk') An error occurred: UNIQUE constraint failed: switches.hostname
Adding data to the dhcp table...
While adding data: ('00:09:BB:3D:D6:58', '10.1.10.2', '10', 'FastEthernet0/1', 'sw1') An error occurred: UNIQUE constraint failed: dhcp.mac
While adding data: ('00:04:A3:3E:5B:69', '10.1.5.2', '5', 'FastEthernet0/10', 'sw1') An error occurred: UNIQUE constraint failed: dhcp.mac
While adding data: ('00:05:B3:7E:9B:60', '10.1.5.4', '5', 'FastEthernet0/9', 'sw1') An error occurred: UNIQUE constraint failed: dhcp.mac
While adding data: ('00:07:BC:3F:A6:50', '10.1.10.6', '10', 'FastEthernet0/3', 'sw1') An error occurred: UNIQUE constraint failed: dhcp.mac
While adding data: ('00:09:BC:3F:A6:50', '192.168.100.100', '1', 'FastEthernet0/7', 'sw1') An error occurred: UNIQUE constraint failed: dhcp.mac
... (the command output is abbreviated)

When creating the database schema, it was explicitly stated that the MAC address
field must be unique. Therefore, when adding an entry with the same MAC address,
an exception (error) is raised. Task 25.1 handles the exception and writes a message
to stdout.

In this task, it is assumed that information is periodically read from
the switches and written to files. After that, the information from the files
must be transferred to the database. At the same time, there may be changes in the
new data: MAC disappeared, MAC switched to another port/vlan, a new MAC appeared, etc.


In this task, in the dhcp table, you need to create a new field, active, which
will indicate whether the record is up-to-date. The new database schema is
located in the dhcp_snooping_schema.sql file.

The active field can have the following values:
* 0 - means False. Used to mark an entry as inactive
* 1 - True. Used to indicate that a record is active

Every time information from files with DHCP snooping output is added again, all
existing entries (for this switch) must be marked as inactive (active = 0).
You can then update the information and mark the new records as active (active = 1).

Thus, the old records will remain in the database for MAC addresses that are
currently inactive, and updated information for active addresses will appear.


For example, the dhcp table contains the following entries:
mac                ip          vlan        interface         switch      active
-----------------  ----------  ----------  ----------------  ----------  ----------
00:09:BB:3D:D6:58  10.1.10.2   10          FastEthernet0/1   sw1         1
00:04:A3:3E:5B:69  10.1.5.2    5           FastEthernet0/10  sw1         1
00:05:B3:7E:9B:60  10.1.5.4    5           FastEthernet0/9   sw1         1
00:07:BC:3F:A6:50  10.1.10.6   10          FastEthernet0/3   sw1         1
00:09:BC:3F:A6:50  192.168.10  1           FastEthernet0/7   sw1         1


And you need to add the following information from the file:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:09:BB:3D:D6:58   10.1.10.2        86250       dhcp-snooping   10    FastEthernet0/1
00:04:A3:3E:5B:69   10.1.15.2        63951       dhcp-snooping   15    FastEthernet0/15
00:05:B3:7E:9B:60   10.1.5.4         63253       dhcp-snooping   5     FastEthernet0/9
00:07:BC:3F:A6:50   10.1.10.6        76260       dhcp-snooping   10    FastEthernet0/5


After adding the data, the table should look like this:
mac                ip               vlan        interface         switch      active
-----------------  ---------------  ----------  ---------------   ----------  ----------
00:09:BC:3F:A6:50  192.168.100.100  1           FastEthernet0/7   sw1         0
00:09:BB:3D:D6:58  10.1.10.2        10          FastEthernet0/1   sw1         1
00:04:A3:3E:5B:69  10.1.15.2        15          FastEthernet0/15  sw1         1
00:05:B3:7E:9B:60  10.1.5.4         5           FastEthernet0/9   sw1         1
00:07:BC:3F:A6:50  10.1.10.6        10          FastEthernet0/5   sw1         1


The new information should overwrite the previous one:
* MAC 00:04:A3:3E:5B:69 went to a different port and got into a different
  interface and got a different IP address
* MAC 00:07:BC:3F:A6:50 switched to another port

If some MAC address is not in the new file, it must be left in the database
with the value active = 0:
* MAC addresses 00:09:BC:3F:A6:50 not in new information (turned off the computer)

Modify the add_data.py script so that the new conditions are met and the active
field is populated.

The code in the script should be broken down into functions. It is up to you to
decide which functions and how to split the code. Some of the code can be global.

To check task and operation of a new field, first add information to the database
from files sw*_dhcp_snooping.txt, and then add information from files
new_data/sw*_dhcp_snooping.txt.


The data should look like this (the lines can be in any order)
-----------------  ---------------  --  ----------------  ---  -
00:09:BC:3F:A6:50  192.168.100.100   1  FastEthernet0/7   sw1  0
00:C5:B3:7E:9B:60  10.1.5.40         5  FastEthernet0/9   sw2  0
00:09:BB:3D:D6:58  10.1.10.2        10  FastEthernet0/1   sw1  1
00:04:A3:3E:5B:69  10.1.15.2        15  FastEthernet0/15  sw1  1
00:05:B3:7E:9B:60  10.1.5.4          5  FastEthernet0/9   sw1  1
00:07:BC:3F:A6:50  10.1.10.6        10  FastEthernet0/5   sw1  1
00:E9:BC:3F:A6:50  100.1.1.6         3  FastEthernet0/20  sw3  1
00:E9:22:11:A6:50  100.1.1.7         3  FastEthernet0/21  sw3  1
00:A9:BB:3D:D6:58  10.1.10.20       10  FastEthernet0/7   sw2  1
00:B4:A3:3E:5B:69  10.1.5.20         5  FastEthernet0/5   sw2  1
00:A9:BC:3F:A6:50  10.1.10.65       20  FastEthernet0/2   sw2  1
00:A9:33:44:A6:50  10.1.10.77       10  FastEthernet0/4   sw2  1
-----------------  ---------------  --  ----------------  ---  -


"""
