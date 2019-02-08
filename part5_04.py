#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 5, Example 4.
"""

# Bigrams

import nltk

F_IN = 'Frankenstein_25.txt'

with open(F_IN, 'r', encoding='utf-8', newline='\n') as f_in:
    raw_text = f_in.read()
    tokens = nltk.word_tokenize(raw_text)
    bigrams = nltk.bigrams(tokens)
    for bigram in bigrams:
        print(bigram)
