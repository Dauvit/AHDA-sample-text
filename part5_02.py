#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 5, Example 2.
"""

# Most frequent words

import nltk

F_IN = 'Frankenstein.txt'

with open(F_IN, 'r', encoding='utf-8', newline='\n') as f_in:
    raw_text = f_in.read()
    tokens = nltk.word_tokenize(raw_text)
    freq_dist = nltk.FreqDist(tokens)
    print(freq_dist.most_common(10))
    print()
    print(freq_dist['monster'])
    print(freq_dist.freq('monster'))
