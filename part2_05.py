#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 2, Example 5.
"""

# Read a json file and display it in a human friendly fashion

import json
import pprint

with open('sample.js', 'r', encoding='utf-8', newline='\n') as f_in:
    json_content = json.load(f_in)
    pprint.pprint(json_content)
