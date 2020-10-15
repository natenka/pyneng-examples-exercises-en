# -*- coding: utf-8 -*-


with open("CAM_table.txt", "r") as conf:
    for line in conf:
        words = line.split()
        if words and words[0].isdigit():
            vlan, mac, _, interface = words
            print(f"{vlan:9}{mac:20}{interface}")
