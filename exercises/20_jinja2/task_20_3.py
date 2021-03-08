# -*- coding: utf-8 -*-
"""
Task 20.3

Create a template templates/ospf.txt based on the OSPF configuration
in the cisco_ospf.txt file. A configuration example is given to show the syntax.

The template must be created manually by copying parts of the config
into the corresponding template.

What values should be variables:
* process number. Variable name - process
* router-id. Variable name - router_id
* reference-bandwidth. Variable name - ref_bw
* interfaces on which to enable OSPF. The variable name is ospf_intf.
  In place of this variable, a list of dictionaries with the following keys is expected:
   * name - interface name, like Fa0/1, Vlan10, Gi0/0
   * ip - interface IP address, like 10.0.1.1
   * area - zone number
   * passive - whether the interface is passive. Valid values: True or False

For all interfaces in the ospf_intf list, you need to generate the following lines:
 network x.x.x.x 0.0.0.0 area x

If the interface is passive, the line must be added for it:
 passive-interface x

For interfaces that are not passive, in interface configuration mode,
you need to add the line:
 ip ospf hello-interval 1


All commands must be in the appropriate configuration mode.

Check the resulting template templates/ospf.txt, against the data in
the data_files/ospf.yml file, using the generate_config function
from task 20.1. Do not copy the code of the generate_config function.

The result should be a configuration of the following type (the commands
in router ospf mode do not have to be in this order, the main thing is that
they are in the correct config section):
router ospf 10
 router-id 10.0.0.1
 auto-cost reference-bandwidth 20000
 network 10.255.0.1 0.0.0.0 area 0
 network 10.255.1.1 0.0.0.0 area 0
 network 10.255.2.1 0.0.0.0 area 0
 network 10.0.10.1 0.0.0.0 area 2
 network 10.0.20.1 0.0.0.0 area 2
 passive-interface Fa0/0.10
 passive-interface Fa0/0.20
interface Fa0/1
 ip ospf hello-interval 1
interface Fa0/1.100
 ip ospf hello-interval 1
interface Fa0/1.200
 ip ospf hello-interval 1
"""
