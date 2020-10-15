# -*- coding: utf-8 -*-

import re


def parse_sh_ip_int_br(textfile):
    regex = r"(\S+) +(\S+) +\w+ \w+ +(administratively down|up|down) +(up|down)"
    with open(textfile) as f:
        result = [m.groups() for m in re.finditer(regex, f.read())]
    return result
