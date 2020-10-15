# -*- coding: utf-8 -*-


access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security",
]

access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}

def generate_access_config(intf_vlan_mapping, access_template, psecurity=None):
    access_config = []

    for intf, vlan in intf_vlan_mapping.items():
        access_config.append(f"interface {intf}")
        for command in access_template:
            if command.endswith("access vlan"):
                access_config.append(f"{command} {vlan}")
            else:
                access_config.append(command)
        if psecurity:
            access_config.extend(psecurity)
    return access_config
