# -*- coding: utf-8 -*-




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

    def send_command(self, command, *args, **kwargs):
        command_output = super().send_command(command, *args, **kwargs)
        self._check_error_in_command(command, command_output)
        return command_output
