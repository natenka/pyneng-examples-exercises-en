# -*- coding: utf-8 -*-

import re


def get_ip_from_cfg(filename):
    result = {}
    regex = (r"^interface (?P<intf>\S+)"
             r"|address (?P<ip>\S+) (?P<mask>\S+)")

    with open(filename) as f:
        for line in f:
            match = re.search(regex, line)
            if match:
                if match.lastgroup == "intf":
                    intf = match.group(match.lastgroup)
                elif match.lastgroup == "mask":
                    result.setdefault(intf, [])
                    result[intf].append(match.group("ip", "mask"))
    return result


# еще один вариант решения

def get_ip_from_cfg(filename):
    result = {}
    with open(filename) as f:
        # сначала отбираем нужные куски конфигурации
        match = re.finditer(
            "interface (\S+)\n"
            "(?: .*\n)*"
            " ip address \S+ \S+\n"
            "( ip address \S+ \S+ secondary\n)*",
            f.read(),
        )
        # потом в этих частях находим все IP-адреса
        for m in match:
            result[m.group(1)] = re.findall("ip address (\S+) (\S+)", m.group())
    return result
