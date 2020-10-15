# -*- coding: utf-8 -*-

import yaml
import glob
from task_17_3 import parse_sh_cdp_neighbors


def generate_topology_from_cdp(list_of_files, save_to_filename=None):
    topology = {}
    for filename in list_of_files:
        with open(filename) as f:
            topology.update(parse_sh_cdp_neighbors(f.read()))
    if save_to_filename:
        with open(save_to_filename, "w") as f_out:
            yaml.dump(topology, f_out, default_flow_style=False)
    return topology


if __name__ == "__main__":
    f_list = glob.glob("sh_cdp_n_*")
    print(generate_topology_from_cdp(f_list, save_to_filename="topology.yaml"))
