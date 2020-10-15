# -*- coding: utf-8 -*-

import re


def get_ints_without_description(config):
    regex = re.compile(r"!\ninterface (?P<intf>\S+)\n"
                       r"(?P<descr> description \S+)?")
    with open(config) as src:
        match = regex.finditer(src.read())
        result = [m.group('intf') for m in match if m.lastgroup == 'intf']
        return result

