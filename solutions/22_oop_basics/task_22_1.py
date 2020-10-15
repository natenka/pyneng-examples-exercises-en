# -*- coding: utf-8 -*-



class Topology:
    def __init__(self, topology_dict):
        self.topology = {}
        for local, remote in topology_dict.items():
            if not self.topology.get(remote) == local:
                self.topology[local] = remote


if __name__ == "__main__":
    top = Topology(topology_example)
    print(top.topology)
