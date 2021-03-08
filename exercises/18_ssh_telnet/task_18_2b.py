# -*- coding: utf-8 -*-
"""
Task 18.2b

Copy the send_config_commands function from task 18.2a and add error checking.

When executing each command, the script should check the output for
the following errors: Invalid input detected, Incomplete command, Ambiguous command


If an error occurs while executing any of the commands, the function should
print a message to the stdout with information about what error occurred,
in which command and on which device, for example:
The "logging" command was executed with the error "Incomplete command." on the device 192.168.100.1

Errors should always be printed, regardless of the value of the log parameter.
At the same time, the log parameter should still control whether the message
"Connecting to 192.168.100.1..." will be displayed.

Send_config_commands should now return a tuple of two dictionaries:
* the first dict with the output of commands that were executed without error
* second dict with the output of commands that were executed with errors

In both dictionaries:
* key - command
* value - output with command execution

You can test the function on one device.


An example of how the send_config_commands function works:

In [16]: commands
Out[16]:
['logging 0255.255.1',
 'logging',
 'a',
 'logging buffered 20010',
 'ip http server']

In [17]: result = send_config_commands(r1, commands)
Connecting to 192.168.100.1...
The "logging 0255.255.1" command was executed with the error "Invalid input detected at '^' marker." on the device 192.168.100.1
The "logging" command was executed with the error "Incomplete command." on the device 192.168.100.1
The "a" command was executed with the error "Ambiguous command:  "a"" on the device 192.168.100.1

In [18]: pprint(result, width=120)
({'ip http server': 'config term\n'
                    'Enter configuration commands, one per line.  End with CNTL/Z.\n'
                    'R1(config)#ip http server\n'
                    'R1(config)#',
  'logging buffered 20010': 'config term\n'
                            'Enter configuration commands, one per line.  End with CNTL/Z.\n'
                            'R1(config)#logging buffered 20010\n'
                            'R1(config)#'},
 {'a': 'config term\n'
       'Enter configuration commands, one per line.  End with CNTL/Z.\n'
       'R1(config)#a\n'
       '% Ambiguous command:  "a"\n'
       'R1(config)#',
  'logging': 'config term\n'
             'Enter configuration commands, one per line.  End with CNTL/Z.\n'
             'R1(config)#logging\n'
             '% Incomplete command.\n'
             '\n'
             'R1(config)#',
  'logging 0255.255.1': 'config term\n'
                        'Enter configuration commands, one per line.  End with CNTL/Z.\n'
                        'R1(config)#logging 0255.255.1\n'
                        '                   ^\n'
                        "% Invalid input detected at '^' marker.\n"
                        '\n'
                        'R1(config)#'})

In [19]: good, bad = result

In [20]: good.keys()
Out[20]: dict_keys(['logging buffered 20010', 'ip http server'])

In [21]: bad.keys()
Out[21]: dict_keys(['logging 0255.255.1', 'logging', 'a'])


Examples of commands with errors:
R1(config)#logging 0255.255.1
                   ^
% Invalid input detected at '^' marker.

R1(config)#logging
% Incomplete command.

R1(config)#a
% Ambiguous command:  "a"
"""

commands_with_errors = ["logging 0255.255.1", "logging", "a"]
correct_commands = ["logging buffered 20010", "ip http server"]

commands = commands_with_errors + correct_commands
