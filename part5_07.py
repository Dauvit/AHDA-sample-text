#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 5, Example 7.
"""

# Stemming words - test your tools

from nltk import LancasterStemmer
from nltk import PorterStemmer

print('LancasterStemmer')
print(LancasterStemmer().stem('nation'))
print(LancasterStemmer().stem('nationality'))
print(LancasterStemmer().stem('nationally'))
print(LancasterStemmer().stem('natural'))
print(LancasterStemmer().stem('naturally'))
print(LancasterStemmer().stem('nature'))
print()
print('PorterStemmer')
print(PorterStemmer().stem('nation'))
print(PorterStemmer().stem('nationality'))
print(PorterStemmer().stem('nationally'))
print(PorterStemmer().stem('natural'))
print(PorterStemmer().stem('naturally'))
print(PorterStemmer().stem('nature'))
