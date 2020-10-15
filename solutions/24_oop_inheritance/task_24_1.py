# -*- coding: utf-8 -*-


from base_connect_class import BaseSSH


class CiscoSSH(BaseSSH):
    def __init__(self, **device_params):
        super().__init__(**device_params)
        self.ssh.enable()
