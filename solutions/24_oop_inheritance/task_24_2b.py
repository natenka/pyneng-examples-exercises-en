# -*- coding: utf-8 -*-


from netmiko.cisco.cisco_ios import CiscoIosSSH
import re
from task_24_2a import ErrorInCommand


class MyNetmiko(CiscoIosSSH):
    def __init__(self, **device_params):
        super().__init__(**device_params)
        self.enable()

    def _check_error_in_command(self, command, result):
        regex = "% (?P<err>.+)"
        message = (
            'При выполнении команды "{cmd}" на устройстве {device} '
            'возникла ошибка "{error}"'
        )
        error_in_cmd = re.search(regex, result)
        if error_in_cmd:
            raise ErrorInCommand(
                message.format(
                    cmd=command, device=self.host, error=error_in_cmd.group("err")
                )
            )

    def send_command(self, command):
        command_output = super().send_command(command)
        self._check_error_in_command(command, command_output)
        return command_output

    def send_config_set(self, commands):
        if isinstance(commands, str):
            commands = [commands]
        commands_output = ""
        self.config_mode()
        for command in commands:
            result = super().send_config_set(command, exit_config_mode=False)
            commands_output += result
            self._check_error_in_command(command, result)
        self.exit_config_mode()
        return commands_output
