# -*- coding: utf-8 -*-

import yaml
from draw_network_graph import draw_topology


def transform_topology(topology_filename):
    with open(topology_filename) as f:
        raw_topology = yaml.load(f)

    formatted_topology = {}
    for l_device, peer in raw_topology.items():
        for l_int, remote in peer.items():
            r_device, r_int = list(remote.items())[0]
            if not (r_device, r_int) in formatted_topology:
                formatted_topology[(l_device, l_int)] = (r_device, r_int)
    return formatted_topology


if __name__ == "__main__":
    formatted_topology = transform_topology("topology.yaml")
    draw_topology(formatted_topology)
