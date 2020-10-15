# -*- coding: utf-8 -*-

import re
import csv
import glob


def parse_sh_version(sh_ver_output):
    regex = (
        "Cisco IOS .*? Version (?P<ios>\S+), .*"
        "uptime is (?P<uptime>[\w, ]+)\n.*"
        'image file is "(?P<image>\S+)".*'
    )
    match = re.search(regex, sh_ver_output, re.DOTALL,)
    if match:
        return match.group("ios", "image", "uptime")


def write_inventory_to_csv(data_filenames, csv_filename):
    headers = ["hostname", "ios", "image", "uptime"]
    with open(csv_filename, "w") as f:
        writer = csv.writer(f)
        writer.writerow(headers)

        for filename in data_filenames:
            hostname = re.search("sh_version_(\S+).txt", filename).group(1)
            with open(filename) as f:
                parsed_data = parse_sh_version(f.read())
                if parsed_data:
                    writer.writerow([hostname] + list(parsed_data))


if __name__ == "__main__":
    sh_version_files = glob.glob("sh_vers*")
    write_inventory_to_csv(sh_version_files, "routers_inventory.csv")
