# -*- coding: utf-8 -*-
"""
Task 9.1

Create generate_access_config function that generates configuration
for access ports.

The function expects arguments:

- a dictionary with interface as a key and VLAN as a value:
     {'FastEthernet0/12': 10,
      'FastEthernet0/14': 11,
      'FastEthernet0/16': 17}
- access ports configuration template as a list of commands (access_mode_template list)

The function should return a list of all ports in access mode with configuration
based on the access_mode_template template.

In this task, the beginning of the function is written and you just need to
continue writing the function body itself.


An example of a final list (each string is written on a new line for readability):
[
'interface FastEthernet0/12',
'switchport mode access',
'switchport access vlan 10',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable',
'interface FastEthernet0/17',
'switchport mode access',
'switchport access vlan 150',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable',
...]

Check the operation of the function using the access_config dictionary
and the list of commands access_mode_template.
If the previous check was successful, check the function again using the dictionary
access_config_2 and make sure that the final list contains the correct interface
numbers and vlans.

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""

access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}

access_config_2 = {
    "FastEthernet0/3": 100,
    "FastEthernet0/7": 101,
    "FastEthernet0/9": 107,
}


def generate_access_config(intf_vlan_mapping, access_template):
    """
    intf_vlan_mapping is a dictionary with interface-VLAN mapping:
         {'FastEthernet0/12': 10,
          'FastEthernet0/14': 11,
          'FastEthernet0/16': 17}
    access_template - list of commands for the port in access mode

    Returns a list of commands.
    """
