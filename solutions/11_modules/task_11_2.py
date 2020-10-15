# -*- coding: utf-8 -*-

from task_11_1 import parse_cdp_neighbors
from draw_network_graph import draw_topology
from pprint import pprint


def create_network_map(filenames):
    network_map = {}

    for filename in filenames:
        with open(filename) as show_command:
            parsed = parse_cdp_neighbors(show_command.read())
            for key, value in parsed.items():
                if not network_map.get(value) == key:
                    network_map[key] = value
    return network_map


# второй вариант
def create_network_map(filenames):
    network_map = {}

    for filename in filenames:
        with open(filename) as show_command:
            parsed = parse_cdp_neighbors(show_command.read())
            for key, value in parsed.items():
                key, value = sorted([key, value])
                network_map[key] = value
    return network_map


if __name__ == "__main__":
    infiles = [
        "sh_cdp_n_sw1.txt",
        "sh_cdp_n_r1.txt",
        "sh_cdp_n_r2.txt",
        "sh_cdp_n_r3.txt",
    ]

    topology = create_network_map(infiles)
    pprint(topology)
    draw_topology(topology)

