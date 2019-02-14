#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 2, Example 6.
"""

# Read an XML file

from xml.etree.ElementTree import XML

with open('sample.xml', 'r', encoding='utf-8', newline='\n') as f_in:
    xml_content = f_in.read()
    tree = XML(xml_content)

    print(tree)
