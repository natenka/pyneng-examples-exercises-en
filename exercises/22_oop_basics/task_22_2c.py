# -*- coding: utf-8 -*-

"""
Task 22.2c

Copy the CiscoTelnet class from task 22.2b and modify the send_config_commands
method to check for errors.

The send_config_commands method must have an additional strict parameter:
* strict=True means that when an error is encountered, a ValueError must
  be raised (default)
* strict=False means that when an error is found, you only need to print
  the error message to the stdout

The method should return output similar to the send_config_set method of
netmiko (example output below). The text of the exception and error in
the example below.

An example of creating an instance of a class:
In [1]: from task_22_2c import CiscoTelnet

In [2]: r1_params = {
   ...:     'ip': '192.168.100.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}

In [3]: r1 = CiscoTelnet(**r1_params)

In [4]: commands_with_errors = ['logging 0255.255.1', 'logging', 'a']
In [5]: correct_commands = ['logging buffered 20010', 'ip http server']
In [6]: commands = commands_with_errors+correct_commands

Using the send_config_commands method:

In [7]: print(r1.send_config_commands(commands, strict=False))
When executing the command "logging 0255.255.1" on device 192.168.100.1, an error occurred -> Invalid input detected at '^' marker.
When executing the command "logging" on device 192.168.100.1, an error occurred -> Incomplete command.
When executing the command "a" on device 192.168.100.1, an error occurred -> Ambiguous command:  "a"
conf t
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#logging 0255.255.1
                   ^
% Invalid input detected at '^' marker.

R1(config)#logging
% Incomplete command.

R1(config)#a
% Ambiguous command:  "a"
R1(config)#logging buffered 20010
R1(config)#ip http server
R1(config)#end
R1#

In [8]: print(r1.send_config_commands(commands, strict=True))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-8-0abc1ed8602e> in <module>
----> 1 print(r1.send_config_commands(commands, strict=True))

...

ValueError: When executing the command "logging 0255.255.1" on device 192.168.100.1, an error occurred -> Invalid input detected at '^' marker.

"""
