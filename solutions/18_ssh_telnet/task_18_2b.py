# -*- coding: utf-8 -*-

import re
from netmiko import ConnectHandler
import yaml

# списки команд с ошибками и без:
commands_with_errors = ["logging 0255.255.1", "logging", "i"]
correct_commands = ["logging buffered 20010", "ip http server"]
commands = commands_with_errors + correct_commands


def send_config_commands(device, config_commands, log=True):
    good_commands = {}
    bad_commands = {}
    error_message = 'Команда "{}" выполнилась с ошибкой "{}" на устройстве {}'
    regex = "% (?P<errmsg>.+)"

    if log:
        print("Подключаюсь к {}...".format(device["host"]))
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        for command in config_commands:
            result = ssh.send_config_set(command, exit_config_mode=False)
            error_in_result = re.search(regex, result)
            if error_in_result:
                print(
                    error_message.format(
                        command, error_in_result.group("errmsg"), ssh.host
                    )
                )
                bad_commands[command] = result
            else:
                good_commands[command] = result
        ssh.exit_config_mode()
    return good_commands, bad_commands


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        print(send_config_commands(dev, commands))
