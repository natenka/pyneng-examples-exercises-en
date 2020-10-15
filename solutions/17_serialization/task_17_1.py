# -*- coding: utf-8 -*-

import csv
import re
import glob


def write_dhcp_snooping_to_csv(filenames, output):
    regex = r"(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)"
    with open(output, "w") as dest:
        writer = csv.writer(dest)
        writer.writerow(["switch", "mac", "ip", "vlan", "interface"])
        for filename in filenames:
            switch = re.search("([^/]+)_dhcp_snooping.txt", filename).group(1)
            with open(filename) as f:
                for line in f:
                    match = re.search(regex, line)
                    if match:
                        writer.writerow((switch,) + match.groups())


if __name__ == "__main__":
    sh_dhcp_snoop_files = glob.glob("*_dhcp_snooping.txt")
    write_dhcp_snooping_to_csv(sh_dhcp_snoop_files, "example_csv.csv")
