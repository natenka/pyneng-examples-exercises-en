# -*- coding: utf-8 -*-
"""
Task 18.3

Create a send_commands function (use netmiko to connect via SSH).

Function parameters:
* device - a dictionary with parameters for connecting to one device
* show - one show command (string)
* config - a list with commands to be executed in configuration mode

The show and config arguments should only be passed as keyword arguments.
Passing these arguments as positional should raise a TypeError exception.

In [4]: send_commands(r1, 'sh clock')
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-4-75adcfb4a005> in <module>
----> 1 send_commands(r1, 'sh clock')

TypeError: send_commands() takes 1 positional argument but 2 were given

Depending on which argument was passed, the send_commands function calls
different functions internally. When calling the send_commands function,
only one of the show, config arguments should always be passed. If both
arguments are passed, a ValueError exception should be raised.

A combination of an argument and a corresponding function:
* show - the send_show_command function from task 18.1
* config - send_config_commands function from task 18.2

The function returns a string with the results of executing single command
or multiple commands.

Check function operation:
* with a list of config commands in variable commands
* single show command in variable command

An example of how the function works:

In [14]: send_commands(r1, show='sh clock')
Out[14]: '*17:06:12.278 UTC Wed Mar 13 2019'

In [15]: commands = ['username user5 password pass5', 'username user6 password pass6']

In [16]: send_commands(r1, config=commands)
Out[16]: 'config term\nEnter configuration commands, one per line.  End with CNTL/Z.\nR1(config)#username user5 password pass5\nR1(config)#username user6 password pass6\nR1(config)#end\nR1#'

"""

commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]
command = "sh ip int br"
