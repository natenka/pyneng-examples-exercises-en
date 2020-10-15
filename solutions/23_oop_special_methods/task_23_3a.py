# -*- coding: utf-8 -*-



class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)

    def _normalize(self, topology_dict):
        normalized_topology = {}
        for box, neighbor in topology_dict.items():
            if not neighbor in normalized_topology:
                normalized_topology[box] = neighbor
        return normalized_topology

    def __add__(self, other):
        return Topology({**self.topology, **other.topology})

    def __iter__(self):
        return iter(self.topology.items())
