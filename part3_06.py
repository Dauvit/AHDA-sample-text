#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part , Example 6.
"""

# Download a json file

import json
from urllib.request import urlopen

URL = 'http://oro.open.ac.uk/cgi/export/eprint/41117/JSON/oro-eprint-41117.js'
SAVE_FILE = 'sample_json_download.js'

with urlopen(URL) as f_in:
    json_file = json.loads(f_in.read().decode('utf-8'))

with open(SAVE_FILE, 'w', encoding='utf-8', newline='\n') as f_out:
    json.dump(json_file, f_out)
