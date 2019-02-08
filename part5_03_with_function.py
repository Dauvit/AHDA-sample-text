#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 5, Example 3.
"""

# Frequency Distribution across more than one text/corpora

import nltk


def get_tokens(file_name, condition):
    """Return a list of tokens extracted from file_name."""
    with open(file_name, 'r', encoding='utf-8',newline='\n') as f_in:
        raw_text = f_in.read()
        tokens = nltk.word_tokenize(raw_text)
        return [(condition, token) for token in tokens]


Frankenstein_tokens = get_tokens('Frankenstein.txt', 'Frankenstein')
print(Frankenstein_tokens[:4])
Moore_tokens = get_tokens('sample_thomas_moore_download.txt', 'Moore')
print(Moore_tokens[:4])
Frankenstein_tokens += Moore_tokens
cfd = nltk.ConditionalFreqDist(Frankenstein_tokens)
print(cfd.conditions())
print(cfd['Frankenstein'])
print(cfd['Frankenstein'].most_common(10))
print(cfd['Moore'])
print(cfd['Moore'].most_common(10))
