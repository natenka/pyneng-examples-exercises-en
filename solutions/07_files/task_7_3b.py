# -*- coding: utf-8 -*-

user_vlan = input("Enter VLAN number: ")

with open("CAM_table.txt", "r") as conf:
    for line in conf:
        words = line.split()
        if words and words[0].isdigit() and words[0] == user_vlan:
            vlan, mac, _, intf = words
            print(f"{vlan:9}{mac:20}{intf}")
