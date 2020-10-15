# -*- coding: utf-8 -*-

import os
from pprint import pprint
from netmiko import ConnectHandler
import yaml


def send_and_parse_show_command(device_dict, command, templates_path):
    if "NET_TEXTFSM" not in os.environ:
        os.environ["NET_TEXTFSM"] = templates_path
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        output = ssh.send_command(command, use_textfsm=True)
    return output


if __name__ == "__main__":
    full_pth = os.path.join(os.getcwd(), "templates")
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        result = send_and_parse_show_command(
            dev, "sh ip int br", templates_path=full_pth
        )
        pprint(result, width=120)

# Второй вариант без использования use_textfsm в netmiko
from task_21_3 import parse_command_dynamic


def send_and_parse_show_command(device_dict, command, templates_path, index="index"):
    attributes = {"Command": command, "Vendor": device_dict["device_type"]}
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        output = ssh.send_command(command)
        parsed_data = parse_command_dynamic(
            output, attributes, templ_path=templates_path, index_file=index
        )
    return parsed_data


if __name__ == "__main__":
    full_pth = os.path.join(os.getcwd(), "templates")
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        result = send_and_parse_show_command(
            dev, "sh ip int br", templates_path=full_pth
        )
        pprint(result, width=120)
