# -*- coding: utf-8 -*-

from itertools import repeat
from concurrent.futures import ThreadPoolExecutor, as_completed

from netmiko import ConnectHandler, NetMikoTimeoutException
import yaml


commands = {
    "192.168.100.1": "sh ip int br",
    "192.168.100.2": "sh arp",
    "192.168.100.3": "sh ip int br",
}


def send_show_command(device, command):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
        prompt = ssh.find_prompt()
    return f"{prompt}{command}\n{result}\n"


def send_command_to_devices(devices, commands_dict, filename, limit=3):
    with ThreadPoolExecutor(max_workers=limit) as executor:
        futures = [
            executor.submit(send_show_command, device, commands_dict[device["host"]])
            for device in devices
        ]
        with open(filename, "w") as f:
            for future in as_completed(futures):
                f.write(future.result())


if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
        devices = yaml.load(f)
    send_command_to_devices(devices, commands, "result.txt")
