# -*- coding: utf-8 -*-

import re


def parse_sh_cdp_neighbors(command_output):
    regex = re.compile(
        r"(?P<r_dev>\w+)  +(?P<l_intf>\S+ \S+)"
        r"  +\d+  +[\w ]+  +\S+ +(?P<r_intf>\S+ \S+)"
    )
    connect_dict = {}
    l_dev = re.search(r"(\S+)[>#]", command_output).group(1)
    connect_dict[l_dev] = {}
    for match in regex.finditer(command_output):
        r_dev, l_intf, r_intf = match.group("r_dev", "l_intf", "r_intf")
        connect_dict[l_dev][l_intf] = {r_dev: r_intf}
    return connect_dict


if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        print(parse_sh_cdp_neighbors(f.read()))
