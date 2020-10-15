# -*- coding: utf-8 -*-


mac = "AAAA:BBBB:CCCC"

# Вариант решения с помощью функции bin
bin_mac = bin(int(mac.replace(":", ""), 16))[2:]
print(bin_mac)

# Вариант решения с форматированием строк
bin_mac = "{:b}".format(int(mac.replace(":", ""), 16))
print(bin_mac)
