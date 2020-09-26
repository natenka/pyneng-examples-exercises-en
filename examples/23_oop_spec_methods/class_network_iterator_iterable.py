import ipaddress

# Iterator
class Network:
    def __init__(self, network):
        self.network = network
        subnet = ipaddress.ip_network(self.network)
        self.addresses = [str(ip) for ip in subnet.hosts()]
        self._index = 0

    def __iter__(self):
        print("Calling __iter__")
        return self

    def __next__(self):
        print("Calling __next__")
        if self._index < len(self.addresses):
            current_address = self.addresses[self._index]
            self._index += 1
            return current_address
        else:
            raise StopIteration


net1 = Network("10.1.1.192/30")

for ip in net1:
    print(ip)

"""
Calling __iter__
Calling __next__
10.1.1.193
Calling __next__
10.1.1.194
Calling __next__
"""

# Iterable
class Network:
    def __init__(self, network):
        self.network = network
        subnet = ipaddress.ip_network(self.network)
        self.addresses = [str(ip) for ip in subnet.hosts()]

    def __iter__(self):
        return iter(self.addresses)


net1 = Network("10.1.1.192/30")

for ip in net1:
    print(ip)
