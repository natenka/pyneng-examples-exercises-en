# -*- coding: utf-8 -*-

from sys import argv

ignore = ["duplex", "alias", "Current configuration"]

src_file, dst_file = argv[1:]

with open(src_file) as src, open(dst_file, 'w') as dst:
    for line in src:
        for ignore_word in ignore:
            if line.startswith("!") or ignore_word in line:
                break
        else:
            dst.write(line)
