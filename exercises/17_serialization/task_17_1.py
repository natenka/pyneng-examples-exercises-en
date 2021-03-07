# -*- coding: utf-8 -*-
"""
Task 17.1

Create the write_dhcp_snooping_to_csv function, which processes the output
of the show dhcp snooping binding command from different files and writes
the processed data to the csv file.

Function arguments:
* filenames - list of filenames with "show dhcp snooping binding" command output
* output - the name of the csv file into which the result will be written

The function returns None.

For example, if a list with one file sw3_dhcp_snooping.txt was passed as an argument:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20
00:E9:22:11:A6:50   100.1.1.7        76260       dhcp-snooping   3    FastEthernet0/21
Total number of bindings: 2

The resulting csv file should contain the following content:
switch,mac,ip,vlan,interface
sw3,00:E9:BC:3F:A6:50,100.1.1.6,3,FastEthernet0/20
sw3,00:E9:22:11:A6:50,100.1.1.7,3,FastEthernet0/21

The first column in the csv file, the name of the switch, must be obtained from
the file name, the rest - from the contents in the files.

Check the function on the contents of the files sw1_dhcp_snooping.txt,
sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt.
"""
