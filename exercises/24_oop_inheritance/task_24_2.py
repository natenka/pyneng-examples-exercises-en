# -*- coding: utf-8 -*-

"""
Task 24.2

Create a MyNetmiko class that inherits the CiscoIosSSH class from netmiko.
Write the __init__ method in the MyNetmiko class so that after connecting
via SSH, it switches to enable mode.

To do this, the __init__ method must first call the __init__ method of
the CiscoIosSSH class, and then switch to enable mode.

Check that the send_command and send_config_set methods are available
in the MyNetmiko class (they are inherited automatically, this is just for checking).

In [2]: from task_24_2 import MyNetmiko

In [3]: r1 = MyNetmiko(**device_params)

In [4]: r1.send_command('sh ip int br')
Out[4]: 'Interface                  IP-Address      OK? Method Status                Protocol\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up      \nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \nEthernet0/2                190.16.200.1    YES NVRAM  up                    up      \nEthernet0/3                192.168.230.1   YES NVRAM  up                    up      \nEthernet0/3.100            10.100.0.1      YES NVRAM  up                    up      \nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      '

"""
from netmiko.cisco.cisco_ios import CiscoIosSSH


device_params = {
    "device_type": "cisco_ios",
    "ip": "192.168.100.1",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
}
