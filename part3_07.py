#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 3, Example 7.
"""

# Download an xml file

from urllib.request import urlopen

URL = 'http://oro.open.ac.uk/cgi/export/eprint/41117/RIOXX2/oro-eprint-41117.xml'
SAVE_FILE = 'sample_xml_download.xml'

with urlopen(URL) as f_in:
    xml_file = f_in.read().decode('utf-8')

with open(SAVE_FILE, 'w', encoding='utf-8', newline='\n') as f_out:
    f_out.write(xml_file)
