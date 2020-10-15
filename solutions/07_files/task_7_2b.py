# -*- coding: utf-8 -*-

from sys import argv

ignore = ["duplex", "alias", "Current configuration"]

src_file, dst_file = argv[1], "config_sw1_cleared.txt"

with open(src_file) as src, open(dst_file, 'w') as dst:
    for line in src:
        skip_line = False
        for ignore_word in ignore:
            if ignore_word in line:
                skip_line = True
                break
        if not line.startswith("!") and not skip_line:
            dst.write(line)

# вариант решения  с for/else
with open(src_file) as src, open(dst_file, 'w') as dst:
    for line in src:
        for ignore_word in ignore:
            if line.startswith("!") or ignore_word in line:
                break
        else:
            dst.write(line)
