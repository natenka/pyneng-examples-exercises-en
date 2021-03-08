# -*- coding: utf-8 -*-

"""
Task 22.2a

Copy the CiscoTelnet class from job 22.2 and modify the send_show_command method
by adding three parameters:
* parse - controls what will be returned: normal command output or a list of dicts
  received after parsing command output using TextFSM.
  If parse=True, a list of dicts should be returned, and parse=False normal output.
  The default is True.
* templates - path to the directory with templates. The default is "templates"
* index is the name of the file where the correspondence between commands and
  templates is stored. The default is "index"

An example of creating an instance of a class:

In [1]: r1_params = {
   ...:     'ip': '192.168.100.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}

In [2]: from task_22_2a import CiscoTelnet

In [3]: r1 = CiscoTelnet(**r1_params)

Using the send_show_command method:
In [4]: r1.send_show_command("sh ip int br", parse=True)
Out[4]:
[{'intf': 'Ethernet0/0',
  'address': '192.168.100.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/1',
  'address': '192.168.200.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/2',
  'address': '192.168.130.1',
  'status': 'up',
  'protocol': 'up'}]

In [5]: r1.send_show_command("sh ip int br", parse=False)
Out[5]: 'sh ip int br\r\nInterface                  IP-Address      OK? Method Status
Protocol\r\nEthernet0/0                192.168.100.1   YES NVRAM  up
up      \r\nEthernet0/1                192.168.200.1   YES NVRAM  up...'


"""
