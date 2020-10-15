# -*- coding: utf-8 -*-

import textfsm


def parse_command_output(template, command_output):
    with open(template) as tmpl:
        parser = textfsm.TextFSM(tmpl)
        header = parser.header
        result = parser.ParseText(command_output)
    return [header] + result


if __name__ == "__main__":
    with open("output/sh_ip_int_br.txt") as show:
        output = show.read()
    result = parse_command_output("templates/sh_ip_int_br.template", output)
    print(result)
