# -*- coding: utf-8 -*-

import yaml
from task_18_1 import send_show_command
from task_18_2 import send_config_commands


commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]
command = "sh ip int br"


def send_commands(device, config=None, show=None):
    if show:
        return send_show_command(device, show)
    elif config:
        return send_config_commands(device, config)


if __name__ == "__main__":
    commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]
    command = "sh ip int br"
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    r1 = devices[0]
    print(send_commands(r1, config=commands))
    print(send_commands(r1, show=command))
