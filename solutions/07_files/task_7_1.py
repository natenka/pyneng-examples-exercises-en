# -*- coding: utf-8 -*-


output = "\n{:25} {}" * 5

with open("ospf.txt", "r") as f:
    for line in f:
        route = line.replace(",", " ").replace("[", "").replace("]", "")
        route = route.split()

        print(output.format(
                "Prefix", route[1],
                "AD/Metric", route[2],
                "Next-Hop", route[4],
                "Last update", route[5],
                "Outbound Interface", route[6],
        ))
