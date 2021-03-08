# -*- coding: utf-8 -*-

"""
Task 24.2b

Copy the class MyNetmiko from task 24.2a.

Add error checking to the send_config_set method using
the _check_error_in_command method.

The send_config_set method should send commands one at a time and check each for errors.
If no errors are encountered while executing the commands, the send_config_set method
returns the output of the commands.

In [2]: from task_24_2b import MyNetmiko

In [3]: r1 = MyNetmiko(**device_params)

In [4]: r1.send_config_set('lo')
---------------------------------------------------------------------------
ErrorInCommand                            Traceback (most recent call last)
<ipython-input-2-8e491f78b235> in <module>()
----> 1 r1.send_config_set('lo')

...
ErrorInCommand: When executing the command "lo" on device 192.168.100.1, an error occurred "Incomplete command."

"""
