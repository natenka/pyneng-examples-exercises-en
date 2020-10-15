# -*- coding: utf-8 -*-


def get_int_vlan_map(config_filename):
    access_port_dict = {}
    trunk_port_dict = {}
    with open(config_filename) as f:
        for line in f:
            if "interface FastEthernet" in line:
                current_interface = line.split()[-1]
                # Сразу указываем, что интерфейсу
                # соответствует 1 влан в access_port_dict
                access_port_dict[current_interface] = 1
            elif "switchport access vlan" in line:
                # если нашлось другое значение VLAN,
                # оно перепишет предыдущее соответствие
                access_port_dict[current_interface] = int(line.split()[-1])
            elif "switchport trunk allowed vlan" in line:
                vlans = [int(i) for i in line.split()[-1].split(",")]
                trunk_port_dict[current_interface] = vlans
                # если встретилась команда trunk allowed vlan
                # надо удалить интерфейс из словаря access_port_dict
                del access_port_dict[current_interface]
    return access_port_dict, trunk_port_dict

