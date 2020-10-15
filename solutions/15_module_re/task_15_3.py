# -*- coding: utf-8 -*-

import re


def convert_ios_nat_to_asa(cisco_ios, cisco_asa):
    regex = (
        "tcp (?P<local_ip>\S+) +(?P<lport>\d+) +interface +\S+ (?P<outside_port>\d+)"
    )
    asa_template = (
        "object network LOCAL_{local_ip}\n"
        " host {local_ip}\n"
        " nat (inside,outside) static interface service tcp {lport} {outside_port}\n"
    )
    with open(cisco_ios) as f, open(cisco_asa, "w") as asa_nat_cfg:
        data = re.finditer(regex, f.read())
        for match in data:
            asa_nat_cfg.write(asa_template.format(**match.groupdict()))


if __name__ == "__main__":
    convert_ios_nat_to_asa("cisco_nat_config.txt", "cisco_asa_config.txt")
