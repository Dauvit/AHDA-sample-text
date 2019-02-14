#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 1, Example 6.
"""

# More with lists

words = ['Mary', 'had', 'a', 'little', 'lamb']

if 'Mary' in words:
    print('Found Mary')
else:
    print('Where has Mary gone?')

target_animal = 'lamb'

if target_animal in words:
    print('Found animal')
else:
    print('Where has the animal gone?')
