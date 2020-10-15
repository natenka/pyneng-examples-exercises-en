# -*- coding: utf-8 -*-

from task_20_1 import generate_config

data = {
    "tun_num": 10,
    "wan_ip_1": "192.168.100.1",
    "wan_ip_2": "192.168.100.2",
    "tun_ip_1": "10.0.1.1 255.255.255.252",
    "tun_ip_2": "10.0.1.2 255.255.255.252",
}


def create_vpn_config(template1, template2, data_dict):
    cfg1 = generate_config(template1, data_dict)
    cfg2 = generate_config(template2, data_dict)
    return cfg1, cfg2


if __name__ == "__main__":
    template1 = "templates/gre_ipsec_vpn_1.txt"
    template2 = "templates/gre_ipsec_vpn_2.txt"
    vpn1, vpn2 = create_vpn_config(template1, template2, data)
    print(vpn1)
    print(vpn2)
