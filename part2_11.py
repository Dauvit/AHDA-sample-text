#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 2, Example 11.
"""

# Read and write a csv file

import csv

CSV_IN = 'sample.csv'
CSV_OUT = 'sample_edited.csv'
FIELDNAMES = ['RecordNumber', 'Title']

with open(CSV_IN, 'r', encoding='utf-8', newline='\n') as f_in, \
     open(CSV_OUT, 'w', encoding='utf-8', newline='\n') as f_out:
    reader = csv.DictReader(f_in)
    writer = csv.writer(f_out)
    writer.writerow(FIELDNAMES)
    for row in reader:
        writer.writerow([row['RecordNumber'], row['Title']])
        if reader.line_num == 25:
            break
