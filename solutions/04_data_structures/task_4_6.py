# -*- coding: utf-8 -*-


ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

output = "\n{:25} {}" * 5

route = ospf_route.replace(",", " ").replace("[", "").replace("]", "")
route = route.split()

print(output.format(
        "Prefix", route[0],
        "AD/Metric", route[1],
        "Next-Hop", route[3],
        "Last update", route[4],
        "Outbound Interface", route[5],
))
