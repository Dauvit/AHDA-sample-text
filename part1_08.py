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

for key, value in mountains.items():
    print(value)
