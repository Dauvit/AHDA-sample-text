#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 3, Example 03.
"""

# Extract other data from html

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

    tag_title = soup.title
    print(tag_title)
    print()
    # tag_title_text = soup.title.text
    # print(tag_title_text)
    # print()
    # tag_a = soup.a
    # print(tag_a)
    # print()
    # tag_a_all = soup.find_all('a')
    # print(tag_a_all)
    # print()
    # for tag_a in tag_a_all:
        # print(tag_a)
