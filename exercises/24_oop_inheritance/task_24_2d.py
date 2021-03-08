# -*- coding: utf-8 -*-

"""
Task 24.2d

Copy class MyNetmiko from task 24.2c or task 24.2b.

Add the ignore_errors parameter to the send_config_set method.
If ignore_errors=True, no error checking is needed and the method
should work exactly like the send_config_set method in netmiko.
If ignore_errors=False, errors should be checked.

By default, errors should be ignored.

In [2]: from task_24_2d import MyNetmiko

In [3]: r1 = MyNetmiko(**device_params)

In [6]: r1.send_config_set('lo')
Out[6]: 'config term\nEnter configuration commands, one per line.  End with CNTL/Z.\nR1(config)#lo\n% Incomplete command.\n\nR1(config)#end\nR1#'

In [7]: r1.send_config_set('lo', ignore_errors=True)
Out[7]: 'config term\nEnter configuration commands, one per line.  End with CNTL/Z.\nR1(config)#lo\n% Incomplete command.\n\nR1(config)#end\nR1#'

In [8]: r1.send_config_set('lo', ignore_errors=False)
---------------------------------------------------------------------------
ErrorInCommand                            Traceback (most recent call last)
<ipython-input-8-704f2e8d1886> in <module>()
----> 1 r1.send_config_set('lo', ignore_errors=False)

...
ErrorInCommand: When executing the command "lo" on device 192.168.100.1, an error occurred "Incomplete command."
"""
