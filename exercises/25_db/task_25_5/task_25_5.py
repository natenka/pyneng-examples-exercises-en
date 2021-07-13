# -*- coding: utf-8 -*-
"""
Task 25.5

There are no tests for the tasks of the 25th chapter!

After completing tasks 25.1 - 25.5, information about inactive records remains
in the database. And, if some MAC address did not appear in new records,
the record with it may remain in the database forever.

And while it can be useful to see where the MAC address was last located,
it is not very useful to keep this information permanently. Instead, you can
delete a record if, for example, it has been stored in the database for more
than a month.


In order to be able to delete records by date, you need to enter a new field
in which the last time the record was added will be recorded.

The new field is called last_active and must contain a string in the format:
YYYY-MM-DD HH:MM:SS.

In this task you need to:
* change the dhcp table accordingly and add a new field. The table can be
  changed from cli sqlite, but the dhcp_snooping_schema.sql file must also be changed
* modify the add_data.py script to add time to each entry

You can get a string with time and date in the specified format using
the datetime function in an SQL query. The syntax is as follows:

sqlite> insert into dhcp (mac, ip, vlan, interface, switch, active, last_active)
   ...> values ('00:09:BC:3F:A6:50', '192.168.100.100', '1', 'FastEthernet0/7', 'sw1', '0', datetime('now'));

That is, instead of the value that is written to the database, you must
specify datetime('now').

After this command, the following entry will appear in the database:
mac                ip               vlan  interface        switch  active  last_active
-----------------  ---------------  ----  ---------------  ------  ------  -------------------
00:09:BC:3F:A6:50  192.168.100.100  1     FastEthernet0/7  sw1     0       2021-03-09 07:46:31
"""
