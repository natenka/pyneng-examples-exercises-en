# -*- coding: utf-8 -*-

from sys import argv

ignore = ["duplex", "alias", "Current configuration"]

filename = argv[1]

with open(filename) as f:
    for line in f:
        skip_line = False
        for ignore_word in ignore:
            if ignore_word in line:
                skip_line = True
                break
        if not line.startswith("!") and not skip_line:
            print(line.rstrip())

# вариант решения с for/else
with open(filename) as f:
    for line in f:
        for ignore_word in ignore:
            if line.startswith("!") or ignore_word in line:
                break
        else:
            print(line.rstrip())
