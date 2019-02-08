#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 3, Example 02.
"""

# Extract text from html

import html
from urllib.request import urlopen

from bs4 import BeautifulSoup

URL = 'https://www.bbc.com/pidgin'
SAVE_FILE = 'sample_html_download.html'

# if working directly from the web
# with urlopen(URL) as f_in:
    # soup = BeautifulSoup(f_in, 'html.parser')

with open(SAVE_FILE, 'r', encoding='utf-8', newline='\n') as f_in:
    soup = BeautifulSoup(f_in, 'html.parser')
    print(soup.get_text())
