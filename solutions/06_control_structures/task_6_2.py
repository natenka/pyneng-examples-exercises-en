# -*- coding: utf-8 -*-


ip_address = input("введите ip-адрес: ")
oct1 = int(ip_address.split(".")[0])

if ip_address == "255.255.255.255":
    print("local broadcast")
elif ip_address == "0.0.0.0":
    print("unassigned")
elif 1 <= oct1 <= 223:
    print("unicast")
elif 224 <= oct1 <= 239:
    print("multicast")
else:
    print("unused")
