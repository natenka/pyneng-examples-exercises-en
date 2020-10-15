# -*- coding: utf-8 -*-

import yaml
import sys
from netmiko import ConnectHandler
from paramiko.ssh_exception import AuthenticationException


def send_show_command(device, command):
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
            return result
    except AuthenticationException as error:
        print(error)


if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        result = send_show_command(dev, command)
        print(result)
