#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 4, Example 7.
"""

# find relevant text and render it in uppercase

F_IN = 'Moore.txt'

with open(F_IN, 'r', encoding='utf-8', newline='\n') as f_in:
    lines = f_in.readlines()
    for line in lines:
        if line.startswith('ART'):
            print(line.upper())
