# -*- coding: utf-8 -*-

from textfsm import clitable
from pprint import pprint


def parse_command_dynamic(
    command_output, attributes_dict, index_file="index", templ_path="templates"
):

    cli_table = clitable.CliTable(index_file, templ_path)
    cli_table.ParseCmd(command_output, attributes_dict)
    return [dict(zip(cli_table.header, row)) for row in cli_table]


if __name__ == "__main__":
    attributes = {"Command": "show ip int br", "Vendor": "cisco_ios"}
    with open("output/sh_ip_int_br.txt") as f:
        command_output = f.read()
    result = parse_command_dynamic(command_output, attributes)
    pprint(result, width=100)
