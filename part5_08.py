#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 5, Example 8.
"""

# Lemmatize words

from nltk import LancasterStemmer
from nltk import PorterStemmer

print('LancasterStemmer')
print(LancasterStemmer().stem('lying'))
print(LancasterStemmer().stem('lie'))
print()
print('PorterStemmer')
print(PorterStemmer().stem('lying'))
print(PorterStemmer().stem('lie'))
