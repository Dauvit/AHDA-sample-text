#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 4, Example 1.

Please rename:

'sample_thomas_moore_download.txt'

to:

'Moore.txt'

"""

# Cut a subset of a file

F_IN = 'Moore.txt'
F_106 = 'Moore_106.txt'
F_4170 = 'Moore_4170.txt'

# by slicing a string

with open(F_IN, 'r', encoding='utf-8', newline='\n') as f_in:
    raw_text = f_in.read()

with open(F_4170, 'w', encoding='utf-8', newline='\n') as f_out:
    f_out.write(raw_text[:4170])


# alternative by looping through lines

with open(F_IN, 'r', encoding='utf-8', newline='\n') as f_in:
    lines = f_in.readlines()

with open(F_106, 'w', encoding='utf-8', newline='\n') as f_out:
    for i, line in enumerate(lines, start=1):
        f_out.write(line)
        if i == 106:
            break
