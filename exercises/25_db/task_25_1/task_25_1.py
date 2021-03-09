# -*- coding: utf-8 -*-
'''
Task 25.1

There are no tests for the tasks of the 25th chapter!

You need to create two scripts:
1. create_db.py
2. add_data.py

The code in scripts should be broken down into functions.
It is up to you to decide which functions and how to split the code.
Some of the code can be global.


create_db.py - this script should contain the functionality for creating a database:
* check for the presence of a database file
* if the file does not exist, according to the description of the database schema
  in the dhcp_snooping_schema.sql file, the database must be created
* the name of the database file is dhcp_snooping.db

The database should contain two tables (the schema is described
in the dhcp_snooping_schema.sql file):
* switches - it contains data about switches
* dhcp - information obtained from the output
  of sh ip dhcp snooping binding is stored here

An example of script execution when there is no dhcp_snooping.db file:
$ python create_db.py
Database creation...

After creating the file:
$ python create_db.py
Database exists


add_data.py script adds data to the database.
This script should add data from sh ip dhcp snooping binding output
and switch information

Accordingly, there should be two parts in the add_data.py file:
* information about switches is added to the switches table.
  Switch data are in the switches.yml file
* information based on the output of sh ip dhcp snooping binding is added to the dhcp table
 * output from three switches in files: files sw1_dhcp_snooping.txt,
   sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt
 * since the dhcp table has changed, and now there is a switch field, it must
   also be filled. The switch name is derived from the data file name


An example of script execution when the database has not yet been created:
$ python add_data.py
The database does not exist. Before adding data, you need to create it

An example of executing the script for the first time after creating the database:
$ python add_data.py
Adding data to the switches table...
Add data to dhcp table...

An example of script execution after the data has been added to the table
(the order of adding data can be arbitrary, but messages must
output similarly to the output below):

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
While adding data: ('00:E9:BC:3F:A6:50', '100.1.1.6', '3', 'FastEthernet0/20', 'sw3') An error occurred: UNIQUE constraint failed: dhcp.mac
While adding data: ('00:E9:22:11:A6:50', '100.1.1.7', '3', 'FastEthernet0/21', 'sw3') An error occurred: UNIQUE constraint failed: dhcp.mac
While adding data: ('00:A9:BB:3D:D6:58', '10.1.10.20', '10', 'FastEthernet0/7', 'sw2') An error occurred: UNIQUE constraint failed: dhcp.mac
While adding data: ('00:B4:A3:3E:5B:69', '10.1.5.20', '5', 'FastEthernet0/5', 'sw2') An error occurred: UNIQUE constraint failed: dhcp.mac
While adding data: ('00:C5:B3:7E:9B:60', '10.1.5.40', '5', 'FastEthernet0/9', 'sw2') An error occurred: UNIQUE constraint failed: dhcp.mac
While adding data: ('00:A9:BC:3F:A6:50', '10.1.10.60', '20', 'FastEthernet0/2', 'sw2') An error occurred: UNIQUE constraint failed: dhcp.mac


At this stage, both scripts are called with no arguments.

The code in scripts should be broken down into functions.
It is up to you to decide which functions and how to split the code.
Some of the code can be global.
'''
