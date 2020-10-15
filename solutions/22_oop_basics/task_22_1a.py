# -*- coding: utf-8 -*-



class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)

    def _normalize(self, topology_dict):
        return {
            min(local, remote): max(local, remote)
            for local, remote in topology_dict.items()
        }

