#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 4, Example 2.
"""

# Trim_leading space

F_IN = 'Moore_106.txt'
F_OUT = 'Moore_106_trimmed.txt'

with open(F_IN, 'r', encoding='utf-8', newline='\n') as f_in:
    lines = f_in.readlines()

with open(F_OUT, 'w', encoding='utf-8', newline='\n') as f_out:
    for line in lines:
        f_out.write(line.strip() + '\n')
