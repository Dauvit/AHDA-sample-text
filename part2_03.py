#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 2, Example 3.
"""

# Write a file

with open('Frankenstein_25.txt', 'r', encoding='utf-8', newline='\n') as f_in:
    raw_text = f_in.read()

messed_up_text = raw_text.replace('e', '@')

with open('Frankenstein_25_messed_up.txt', 'w', encoding='utf-8', newline='\n') as f_out:
    f_out.write(messed_up_text)
