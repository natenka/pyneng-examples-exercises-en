import re

regex = "Host \S+ " "in vlan (\d+) " "is flapping between port " "(\S+) and port (\S+)"

ports = set()

with open("log.txt") as f:
    for m in re.finditer(regex, f.read()):
        vlan = m.group(1)
        ports.add(m.group(2))
        ports.add(m.group(3))

print("Loop between ports {} in VLAN {}".format(", ".join(ports), vlan))
