# -*- coding: utf-8 -*-

import yaml
import sys
from netmiko import ConnectHandler
from netmiko.ssh_exception import SSHException


def send_show_command(device, command):
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
            return result
    except SSHException as error:
        print(error)


if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    r1 = devices[0]
    result = send_show_command(r1, command)
    print(result)
