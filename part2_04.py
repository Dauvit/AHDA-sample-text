#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 2, Example 4.
"""

# Read a json file

import json

with open('sample.js', 'r', encoding='utf-8', newline='\n') as f_in:
    json_content = json.load(f_in)
    print(json_content)
