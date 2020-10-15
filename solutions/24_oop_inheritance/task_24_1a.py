# -*- coding: utf-8 -*-


from base_connect_class import BaseSSH


class CiscoSSH(BaseSSH):
    def __init__(self, **device_params):
        params = {
            "username": "Введите имя пользователя: ",
            "password": "Введите пароль: ",
            "secret": "Введите пароль для режима enable: ",
        }
        for param in params:
            if not param in device_params:
                device_params[param] = input(params[param])
        super().__init__(**device_params)
        self.ssh.enable()

