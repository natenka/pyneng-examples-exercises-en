# -*- coding: utf-8 -*-


from netmiko.cisco.cisco_ios import CiscoIosSSH


class MyNetmiko(CiscoIosSSH):
    def __init__(self, **device_params):
        super().__init__(**device_params)
        self.enable()
