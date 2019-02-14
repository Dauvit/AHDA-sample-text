#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 1, Example 8.
"""

# A mountainous dictionary

mountains = {'Asia': 'Everest',
             'South America': 'Aconcagua',
             'North America': 'Denali',
             'Africa': 'Kilimanjaro',
             'Antarctica': 'Vinson',
             'Europe': 'Elbrus',
             'Australia': 'Kosciuszko'}

for key in mountains.keys():
    print(key)

print()
for key, value in mountains.items():
    print(f'The highest mountain in {key} is {value}')

print()
for continent, mountain in mountains.items():
    print(f'The highest mountain in {continent} is {mountain}')

print()
print(mountains['Australia'])
