# -*- coding: utf-8 -*-


access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

template = {"access": access_template, "trunk": trunk_template}
question = {"access": "Введите номер VLAN: ", "trunk": "Введите разрешенные VLANы: "}

mode = input("Введите режим работы интерфейса (access/trunk): ")
interface = input("Введите тип и номер интерфейса: ")
vlans = input(question[mode])

print("interface {}".format(interface))
print("\n".join(template[mode]).format(vlans))
