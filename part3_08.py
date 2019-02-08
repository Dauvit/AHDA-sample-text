#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part , Example 8.
"""

# Download a pdf file

from urllib.request import urlopen

URL = 'http://oro.open.ac.uk/41117/1/Finding-agriculture-among-biodiversity-BromleyKingMorse-30-MTSR2014.pdf'
SAVE_FILE = 'sample_pdf_download.pdf'

with urlopen(URL) as f_in:
    pdf_file = f_in.read()

with open(SAVE_FILE, 'wb') as f_out:
    f_out.write(pdf_file)
