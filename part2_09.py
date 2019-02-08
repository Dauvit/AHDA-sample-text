#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 2, Example 9.
"""

# Read a csv file as a list

import csv

CSV_IN = 'sample.csv'

with open(CSV_IN, 'r', encoding='utf-8', newline='\n') as f_csv:
    reader = csv.reader(f_csv)
    for row in reader:
        print(row[4])
        if reader.line_num == 25:
            break
