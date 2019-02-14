#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 4, Example 10.
"""

# looping through all files in a folder


from pathlib import Path

INPUT_FOLDER = '.'
PATTERN = '*.csv'

files_to_read = Path(INPUT_FOLDER).glob(PATTERN)
for file_to_read in files_to_read:
    with open(file_to_read, 'r', encoding='utf-8', newline='\n') as f_in:
        print(file_to_read.name)
        raw_text = f_in.read()
        sample_text = raw_text[:200]
        print(sample_text)
        print()
