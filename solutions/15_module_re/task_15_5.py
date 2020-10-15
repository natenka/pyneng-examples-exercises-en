# -*- coding: utf-8 -*-

import re


def generate_description_from_cdp(sh_cdp_filename):
    regex = re.compile(
        r"(?P<r_dev>\w+)  +(?P<l_intf>\S+ \S+)"
        r"  +\d+  +[\w ]+  +\S+ +(?P<r_intf>\S+ \S+)"
    )
    description = "description Connected to {} port {}"
    intf_desc_map = {}
    with open(sh_cdp_filename) as f:
        for match in regex.finditer(f.read()):
            r_dev, l_intf, r_intf = match.group("r_dev", "l_intf", "r_intf")
            intf_desc_map[l_intf] = description.format(r_dev, r_intf)
    return intf_desc_map


if __name__ == "__main__":
    print(generate_description_from_cdp("sh_cdp_n_sw1.txt"))
