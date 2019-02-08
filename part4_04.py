#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 4, Example 4.
"""

# reduce redundant newlines

import re

NEWLINE_REDUCER = re.compile('\n+').sub

F_IN = 'Moore_106_trimmed.txt'
F_OUT = 'Moore_106_slimmed.txt'

with open(F_IN, 'r', encoding='utf-8', newline='\n') as f_in:
    raw_text = f_in.read()

with open(F_OUT, 'w', encoding='utf-8', newline='\n') as f_out:
    f_out.write(NEWLINE_REDUCER('\n', raw_text))
