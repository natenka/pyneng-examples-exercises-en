# -*- coding: utf-8 -*-
"""
Task 21.1

Create parse_command_output function. Function parameters:
* template - name of the file containing the TextFSM template.
  For example templates/sh_ip_int_br.template
* command_output - output the corresponding show command (string)

The function should return a list:
* the first element is a list with column names
* the rest of the items are lists, which contain the results
  of processing the output of the show command

Check the operation of the function on the output of the sh ip int br command
from the equipment and on the templates/sh_ip_int_br.template template.

"""
from netmiko import ConnectHandler


# this is how a function call should look
if __name__ == "__main__":
    r1_params = {
        "device_type": "cisco_ios",
        "host": "192.168.100.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    }
    with ConnectHandler(**r1_params) as r1:
        r1.enable()
        output = r1.send_command("sh ip int br")
    result = parse_command_output("templates/sh_ip_int_br.template", output)
    print(result)
