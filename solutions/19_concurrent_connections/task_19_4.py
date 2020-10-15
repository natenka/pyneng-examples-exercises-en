# -*- coding: utf-8 -*-

from itertools import repeat
from concurrent.futures import ThreadPoolExecutor, as_completed

from netmiko import ConnectHandler, NetMikoTimeoutException
import yaml


def send_show_command(device, command):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
        prompt = ssh.find_prompt()
    return f"{prompt}{command}\n{result}\n"


def send_cfg_commands(device, commands):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_config_set(commands)
    return f"{result}\n"


def send_commands_to_devices(devices, filename, show=None, config=None, limit=3):
    command = show if show else config
    function = send_show_command if show else send_cfg_commands

    with ThreadPoolExecutor(max_workers=limit) as executor:
        futures = [executor.submit(function, device, command) for device in devices]
        with open(filename, "w") as f:
            for future in as_completed(futures):
                f.write(future.result())


if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
        devices = yaml.load(f)
    send_commands_to_devices(devices, show=command, filename="result.txt")
    send_commands_to_devices(devices, config="logging 10.5.5.5", filename="result.txt")
