#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 4, Example 8.
"""

# extract words

import re

EXTRACT_WORDS = re.compile(r'\w+').findall

F_IN = 'Moore_106_trimmed.txt'

with open(F_IN, 'r', encoding='utf-8', newline='\n') as f_in:
    raw_text = f_in.read()
    words = EXTRACT_WORDS(raw_text)
    print(words)
    print(len(words))
