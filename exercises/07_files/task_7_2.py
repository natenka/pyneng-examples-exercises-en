# -*- coding: utf-8 -*-
"""
Task 7.2

Create a script that will process the config_sw1.txt configuration file.
The filename is passed as an argument to the script.

The script should return to the stdout commands from the passed
configuration file, excluding lines that start with '!'.

There should be no blank lines in the output.

Restriction: All tasks must be done using the topics covered in this and previous chapters.

Output example:

$ python task_7_2.py config_sw1.txt
Current configuration : 2033 bytes
version 15.0
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
hostname sw1
interface Ethernet0/0
 duplex auto
interface Ethernet0/1
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100
 switchport mode trunk
 duplex auto
 spanning-tree portfast edge trunk
interface Ethernet0/2
 duplex auto
interface Ethernet0/3
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100
 duplex auto
 switchport mode trunk
 spanning-tree portfast edge trunk
...

"""
