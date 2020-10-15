# -*- coding: utf-8 -*-

mac_table = []

with open("CAM_table.txt", "r") as conf:
    for line in conf:
        words = line.split()
        if words and words[0].isdigit():
            vlan, mac, _, intf = words
            mac_table.append([int(vlan), mac, intf])

for vlan, mac, intf in sorted(mac_table):
    print(f"{vlan:<9}{mac:20}{intf}")
