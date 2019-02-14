#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 5, Example 1.
"""

# Tokenize text

import nltk

F_IN = 'Frankenstein.txt'

with open(F_IN, 'r', encoding='utf-8', newline='\n') as f_in:
    raw_text = f_in.read()
    tokens = word_tokenize(raw_text)
    print(len(tokens))
    print()
    print(tokens[:10])
