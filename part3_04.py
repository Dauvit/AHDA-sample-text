#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 3, Example 04.
"""

# Download an html file from web 1.0
# written eleven years ago

from urllib.request import urlopen

URL = 'http://www.thomasmoore.ie/Prose/EdRev/TMHA_1.0_Prose_EdRev_1814_23.html'
SAVE_FILE = 'sample_thomas_moore_download.html'

with urlopen(URL) as f_in:
    html_file = f_in.read().decode('utf-8')

with open(SAVE_FILE, 'w', encoding='utf-8', newline='\n') as f_out:
    f_out.write(html_file)
