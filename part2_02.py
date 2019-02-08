#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 2, Example 2.
"""

# Read a file

with open('Frankenstein_25.txt', 'r', encoding='utf-8', newline='\n') as f_in:
    for line in f_in.readlines():
        print(line)
