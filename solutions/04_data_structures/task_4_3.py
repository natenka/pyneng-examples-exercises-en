# -*- coding: utf-8 -*-


config = "switchport trunk allowed vlan 1,3,10,20,30,100"

result = config.split()[-1].split(",")
print(result)
