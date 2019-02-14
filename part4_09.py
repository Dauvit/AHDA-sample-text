#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 4, Example 9.
"""

# remove stop words - pronouns

import re

EXTRACT_WORDS = re.compile(r'\w+').findall

F_IN = 'Moore_106_trimmed.txt'

PRONOUNS = ['her', 'hers', 'herself', 'him', 'himself', 'his',
            'hisself', 'it', 'itself', 'me', 'mine', 'my', 'myself',
            'one', 'oneself', 'our', 'ours', 'ourselves', 'ownself',
            'self', 'she', 'thee', 'their', 'theirs', 'them',
            'themselves', 'they', 'thou', 'thy', 'us', 'your']

with open(F_IN, 'r', encoding='utf-8', newline='\n') as f_in:
    raw_text = f_in.read()
    words = EXTRACT_WORDS(raw_text)
    no_pronouns = [word for word in words if word not in PRONOUNS]
    print(no_pronouns)
    print(len(no_pronouns))
