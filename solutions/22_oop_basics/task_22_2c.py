# -*- coding: utf-8 -*-


import time
import telnetlib
import yaml
from textfsm import clitable
import re


class CiscoTelnet:
    def __init__(self, ip, username, password, secret):
        self.ip = ip
        self.telnet = telnetlib.Telnet(ip)
        self.telnet.read_until(b"Username:")
        self._write_line(username)
        self.telnet.read_until(b"Password:")
        self._write_line(password)
        self._write_line("enable")
        self.telnet.read_until(b"Password:")
        self._write_line(secret)
        self._write_line("terminal length 0")
        time.sleep(1)
        self.telnet.read_very_eager()

    def _write_line(self, line):
        self.telnet.write(line.encode("ascii") + b"\n")

    def send_show_command(self, command, parse=True, templates="templates"):
        self._write_line(command)
        time.sleep(1)
        command_output = self.telnet.read_very_eager().decode("ascii")
        if not parse:
            return command_output
        attributes = {"Command": command, "Vendor": "cisco_ios"}
        cli = clitable.CliTable("index", templates)
        cli.ParseCmd(command_output, attributes)
        return [dict(zip(cli.header, row)) for row in cli]

    def _error_in_command(self, command, result, strict):
        regex = "% (?P<err>.+)"
        template = (
            'При выполнении команды "{cmd}" на устройстве {device} '
            "возникла ошибка -> {error}"
        )
        error_in_cmd = re.search(regex, result)
        if error_in_cmd:
            message = template.format(
                cmd=command, device=self.ip, error=error_in_cmd.group("err")
            )
            if strict:
                raise ValueError(message)
            else:
                print(message)

    def send_config_commands(self, commands, strict=True):
        output = ""
        if isinstance(commands, str):
            commands = [commands]
        self._write_line("conf t")
        for command in commands:
            self._write_line(command)
            time.sleep(1)
            result = self.telnet.read_very_eager().decode("ascii")
            output += result
            self._error_in_command(command, result, strict=strict)
        self._write_line("end")
        time.sleep(1)
        output += self.telnet.read_very_eager().decode("ascii")
        return output


if __name__ == "__main__":
    r1_params = {
        "ip": "192.168.100.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    }
    r1 = CiscoTelnet(**r1_params)
    print(r1.send_config_commands(commands, strict=False))
