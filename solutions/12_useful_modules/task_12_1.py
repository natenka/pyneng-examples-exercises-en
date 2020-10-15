# -*- coding: utf-8 -*-

import subprocess


def ping_ip_addresses(ip_addresses):
    reachable = []
    unreachable = []

    for ip in ip_addresses:
        result = subprocess.run(
            ["ping", "-c", "3", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        if result.returncode == 0:
            reachable.append(ip)
        else:
            unreachable.append(ip)

    return reachable, unreachable


if __name__ == "__main__":
    print(ping_ip_addresses(["10.1.1.1", "8.8.8.8"]))
