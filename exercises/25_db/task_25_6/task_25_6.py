# -*- coding: utf-8 -*-
"""
Task 25.6

There are no tests for the tasks of the 25th chapter!

This task contains the parse_dhcp_snooping.py file.
You cannot change anything in the parse_dhcp_snooping.py file.

The file creates several functions and describes the command line arguments
that the file takes.
There is support for arguments to perform all the actions that, in the previous
tasks, were performed in the files create_db.py, add_data.py and get_data.py.

The parse_dhcp_snooping.py file contains this line:
import parse_dhcp_snooping_functions as pds

And the goal of this task is to create all the necessary functions
in the parse_dhcp_snooping_functions.py file based on the information
in the parse_dhcp_snooping.py file.

From the parse_dhcp_snooping.py file, you need to decide:
* what functions should be in the parse_dhcp_snooping_functions.py file
* what parameters to create in these functions

It is necessary to create the corresponding functions and transfer to them
the functionality that is described in the previous tasks.
All the necessary information is present in the create, add, get functions,
in the parse_dhcp_snooping.py file.

In principle, to complete the task, it is not necessary to understand
the argparse module, but, you can read about it in section:
https://pyneng.readthedocs.io/en/latest/book/additional_info/argparse.html


To make it easier to get started, try creating the required functions
in parse_dhcp_snooping_functions.py and just print the function arguments.
Then, you can create functions that request information from the database
(the database can be copied from previous jobs).

You can create any helper functions in parse_dhcp_snooping_functions.py,
not just those called from parse_dhcp_snooping.py.

Check all operations:
* creating a database
* adding information about switches
* adding information based on the output of sh ip dhcp snooping binding from files
* selection of information from the database (by parameter and all information)

To make it easier to understand what the script call will look like,
here are some examples. The examples show the option when the database has active
and last_active fields, but you can also use the option without these fields.

$ python parse_dhcp_snooping.py get -h
usage: parse_dhcp_snooping.py get [-h] [--db DB_FILE]
                                  [-k {mac,ip,vlan,interface,switch}]
                                  [-v VALUE] [-a]

optional arguments:
  -h, --help            show this help message and exit
  --db DB_FILE          database name
  -k {mac,ip,vlan,interface,switch}
                        parameter for searching records
  -v VALUE              parameter value
  -a                    show all database content


$ python parse_dhcp_snooping.py add -h
usage: parse_dhcp_snooping.py add [-h] [--db DB_FILE] [-s]
                                  filename [filename ...]

positional arguments:
  filename      file(s) to add

optional arguments:
  -h, --help    show this help message and exit
  --db DB_FILE  database name
  -s            if the flag is set, add switch data, otherwise add DHCP
                records


$ python parse_dhcp_snooping.py create_db
Creating a dhcp_snooping.db database with dhcp_snooping_schema.sql schema
Creating database...


$ python parse_dhcp_snooping.py add sw[1-3]_dhcp_snooping.txt
Adding information from files
sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt

Adding data on DHCP records to dhcp_snooping.db


$ python parse_dhcp_snooping.py add -s switches.yml
Adding switch data

$ python parse_dhcp_snooping.py get
The dhcp table has the following entries:

Active entries:

-----------------  ---------------  --  ----------------  ---  -  -------------------
00:09:BB:3D:D6:58  10.1.10.2        10  FastEthernet0/1   sw1  1  2019-03-08 16:47:52
00:04:A3:3E:5B:69  10.1.5.2          5  FastEthernet0/10  sw1  1  2019-03-08 16:47:52
00:05:B3:7E:9B:60  10.1.5.4          5  FastEthernet0/9   sw1  1  2019-03-08 16:47:52
00:07:BC:3F:A6:50  10.1.10.6        10  FastEthernet0/3   sw1  1  2019-03-08 16:47:52
00:09:BC:3F:A6:50  192.168.100.100   1  FastEthernet0/7   sw1  1  2019-03-08 16:47:52
00:A9:BB:3D:D6:58  10.1.10.20       10  FastEthernet0/7   sw2  1  2019-03-08 16:47:52
00:B4:A3:3E:5B:69  10.1.5.20         5  FastEthernet0/5   sw2  1  2019-03-08 16:47:52
00:C5:B3:7E:9B:60  10.1.5.40         5  FastEthernet0/9   sw2  1  2019-03-08 16:47:52
00:A9:BC:3F:A6:50  10.1.10.60       20  FastEthernet0/2   sw2  1  2019-03-08 16:47:52
00:E9:BC:3F:A6:50  100.1.1.6         3  FastEthernet0/20  sw3  1  2019-03-08 16:47:52
-----------------  ---------------  --  ----------------  ---  -  -------------------


$ python parse_dhcp_snooping.py get -k vlan -v 10
Data from the database: dhcp_snooping.db
Information about devices with the following parameters: vlan 10

Active entries:

-----------------  ----------  --  ---------------  ---  -  -------------------
00:09:BB:3D:D6:58  10.1.10.2   10  FastEthernet0/1  sw1  1  2019-03-08 16:47:52
00:07:BC:3F:A6:50  10.1.10.6   10  FastEthernet0/3  sw1  1  2019-03-08 16:47:52
00:A9:BB:3D:D6:58  10.1.10.20  10  FastEthernet0/7  sw2  1  2019-03-08 16:47:52
-----------------  ----------  --  ---------------  ---  -  -------------------


$ python parse_dhcp_snooping.py get -k vln -v 10
usage: parse_dhcp_snooping.py get [-h] [--db DB_FILE]
                                  [-k {mac,ip,vlan,interface,switch}]
                                  [-v VALUE] [-a]
parse_dhcp_snooping.py get: error: argument -k: invalid choice: 'vln' (choose from 'mac', 'ip', 'vlan', 'interface', 'switch')

"""
