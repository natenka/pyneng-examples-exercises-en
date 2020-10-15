# -*- coding: utf-8 -*-

import re

def get_ip_from_cfg(config):
    with open(config) as f:
        regex = re.compile(
            r"interface (?P<intf>\S+)\n"
            r"( .*\n)*"
            r" ip address (?P<ip>\S+) (?P<mask>\S+)"
        )
        match = regex.finditer(f.read())

    result = {m.group("intf"): m.group("ip", "mask") for m in match}
    return result
