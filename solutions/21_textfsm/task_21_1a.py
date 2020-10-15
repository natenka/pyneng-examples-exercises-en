# -*- coding: utf-8 -*-

from pprint import pprint
import textfsm


def parse_output_to_dict(template, command_output):
    with open(template) as tmpl:
        parser = textfsm.TextFSM(tmpl)
        header = parser.header
        result = parser.ParseText(command_output)
    return [dict(zip(parser.header, line)) for line in result]


if __name__ == "__main__":
    with open("output/sh_ip_int_br.txt") as show:
        output = show.read()
    result = parse_output_to_dict("templates/sh_ip_int_br.template", output)
    pprint(result, width=100)


# вариант с ParseTextToDicts
def parse_output_to_dict(template, command_output):
    with open(template) as template:
        fsm = textfsm.TextFSM(template)
        result = fsm.ParseTextToDicts(command_output)
    return result
