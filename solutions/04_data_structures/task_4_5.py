# -*- coding: utf-8 -*-


command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

vlans1 = command1.split()[-1].split(",")
vlans2 = command2.split()[-1].split(",")

intersection = sorted(set(vlans1) & set(vlans2))
print(intersection)
