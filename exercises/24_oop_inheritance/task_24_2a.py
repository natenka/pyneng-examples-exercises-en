# -*- coding: utf-8 -*-

"""
Task 24.2a

Copy and update the MyNetmiko class from task 24.2.

Add the _check_error_in_command method that checks for such errors:
Invalid input detected, Incomplete command, Ambiguous command

The method expects a command and command output as an argument. If no error
is found in the output, the method returns nothing. If an error is found
in the output, the method should raise an ErrorInCommand exception with a message
about which error was detected, on which device, and in which command.

An ErrorInCommand exception is created in the task file.

Rewrite send_command method to include error checking.

In [2]: from task_24_2a import MyNetmiko

In [3]: r1 = MyNetmiko(**device_params)

In [4]: r1.send_command('sh ip int br')
Out[4]: 'Interface                  IP-Address      OK? Method Status                Protocol\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up      \nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \nEthernet0/2                190.16.200.1    YES NVRAM  up                    up      \nEthernet0/3                192.168.230.1   YES NVRAM  up                    up      \nEthernet0/3.100            10.100.0.1      YES NVRAM  up                    up      \nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      '

In [5]: r1.send_command('sh ip br')
---------------------------------------------------------------------------
ErrorInCommand                            Traceback (most recent call last)
<ipython-input-2-1c60b31812fd> in <module>()
----> 1 r1.send_command('sh ip br')
...
ErrorInCommand: When executing the command "sh ip br" on device 192.168.100.1, an error occurred "Invalid input detected at '^' marker."

"""


class ErrorInCommand(Exception):
    """
    An exception is raised if an error occurs while executing
    a command on the device.
    """
