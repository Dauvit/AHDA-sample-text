#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 5, Example 6.
"""

# concordance

import nltk

F_IN = 'Frankenstein.txt'

with open(F_IN, 'r', encoding='utf-8', newline='\n') as f_in:
    raw_text = f_in.read()
    tokens = nltk.word_tokenize(raw_text)
    nltk_text = nltk.Text(tokens)
    print(nltk_text.concordance('monster', lines=5))
