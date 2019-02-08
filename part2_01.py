#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 2, Example 1.
"""

# Read a file

with open('Frankenstein_25.txt', 'r', encoding='utf-8') as f_in:
    for line in f_in.read():
        print(line)
