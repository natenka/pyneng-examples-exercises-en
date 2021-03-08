# -*- coding: utf-8 -*-
"""
Task 20.5

Create templates templates/gre_ipsec_vpn_1.txt and templates/gre_ipsec_vpn_2.txt
that generate IPsec over GRE configuration between two routers.

The templates/gre_ipsec_vpn_1.txt template creates the configuration for one
side of the tunnel, and templates gre_ipsec_vpn_2.txt for the other.

Examples of the final configuration that should be generated from templates
in the files: cisco_vpn_1.txt and cisco_vpn_2.txt.

Templates must be created manually by copying parts of the config into
the corresponding templates.

Create a create_vpn_config function that uses these templates to generate
a VPN configuration based on the data in the data dictionary.

Function parameters:
* template1 - the name of the template file that creates the configuration
  for one side of the tunnel
* template2 - the name of the template file that creates the configuration
  for the second side of the tunnel
* data_dict - a dictionary with values to be substituted into templates

The function must return a tuple with two configurations (strings) that are
derived from templates.

Examples of VPN configurations that the create_vpn_config function
should return in the cisco_vpn_1.txt and cisco_vpn_2.txt files.
"""

data = {
    "tun_num": 10,
    "wan_ip_1": "192.168.100.1",
    "wan_ip_2": "192.168.100.2",
    "tun_ip_1": "10.0.1.1 255.255.255.252",
    "tun_ip_2": "10.0.1.2 255.255.255.252",
}
