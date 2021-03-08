# -*- coding: utf-8 -*-
"""
Task 18.2c

Copy the send_config_commands function from task 18.2b and remake it as follows:
If an error occurs while executing a command, ask the user whether to continue
executing other commands.

Answer options [y]/n:
* y - execute other commands. This is the default, so any key is interpreted as y
* n or no - do not execute other commands

The send_config_commands function should still return a tuple of two dictionaries:
* the first dictionary with the output of commands that were executed without error
* second dictionary with the output of commands that were executed with errors

In both dictionaries:
* key - command
* value - output with command execution

You can test the function on one device.

An example of how the send_config_commands function works:

In [11]: result = send_config_commands(r1, commands)
Connecting to 192.168.100.1...
The "logging 0255.255.1" command was executed with the error "Invalid input detected at '^' marker." on the device 192.168.100.1
Do you want to continue executing commands? [y]/n: y
The "logging" command was executed with the error "Incomplete command." on the device 192.168.100.1
Do you want to continue executing commands? [y]/n: n

In [12]: pprint(result)
({},
 {'logging': 'config term\n'
             'Enter configuration commands, one per line.  End with CNTL/Z.\n'
             'R1(config)#logging\n'
             '% Incomplete command.\n'
             '\n'
             'R1(config)#',
  'logging 0255.255.1': 'config term\n'
                        'Enter configuration commands, one per line.  End with '
                        'CNTL/Z.\n'
                        'R1(config)#logging 0255.255.1\n'
                        '                   ^\n'
                        "% Invalid input detected at '^' marker.\n"
                        '\n'
                        'R1(config)#'})

"""

commands_with_errors = ["logging 0255.255.1", "logging", "a"]
correct_commands = ["logging buffered 20010", "ip http server"]

commands = commands_with_errors + correct_commands
