#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 5, Example 3.
"""

# Frequency Distribution across more than one text/corpora

import nltk

FILE_ONE = 'Frankenstein.txt'
FILE_TWO = 'sample_thomas_moore_download.txt'

with open(FILE_ONE, 'r', encoding='utf-8',newline='\n') as f_in:
    raw_text = f_in.read()
    tokens = nltk.word_tokenize(raw_text)
    Frankenstein_tokens = [('Frankenstein', token) for token in tokens]

with open(FILE_TWO, 'r', encoding='utf-8',newline='\n') as f_in:
    raw_text = f_in.read()
    tokens = nltk.word_tokenize(raw_text)
    Moore_tokens = [('Moore', token) for token in tokens]

print(Frankenstein_tokens[:4])
print(Moore_tokens[:4])
Frankenstein_tokens += Moore_tokens
cfd = nltk.ConditionalFreqDist(Frankenstein_tokens)
print(cfd.conditions())
print(cfd['Frankenstein'])
print(cfd['Frankenstein'].most_common(10))
print(cfd['Moore'])
print(cfd['Moore'].most_common(10))
