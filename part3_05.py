#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 3, Example 05.
"""

# Extract text from static html

import html
from urllib.request import urlopen

from bs4 import BeautifulSoup

URL = 'http://www.thomasmoore.ie/Prose/EdRev/TMHA_1.0_Prose_EdRev_1814_23.html'
HTML_IN = 'sample_thomas_moore_download.html'
TXT_OUT = 'sample_thomas_moore_download.txt'

# if working directly from the web
# with urlopen(URL) as f_in:
    # soup = BeautifulSoup(f_in, 'html.parser')

with open(HTML_IN, 'r', encoding='utf-8', newline='\n') as f_in:
    soup = BeautifulSoup(f_in, 'html.parser')
    soup_text = soup.get_text()
    print(soup_text)

with open(TXT_OUT, 'w', encoding='utf-8', newline='\n') as f_out:
    f_out.write(soup_text)
