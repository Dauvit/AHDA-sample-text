#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 2, Example 7.
"""

# Read an XML file usefully

from xml.etree.ElementTree import XML

with open('sample.xml', 'r', encoding='utf-8', newline='\n') as f_in:
    xml_content = f_in.read()
    tree = XML(xml_content)

    for branch in tree:
        print(branch)
        print(branch.tag)
        print(branch.text)
        print()

    for author in tree.findall('{http://docs.rioxx.net/schema/v2.0/rioxxterms/}author'):
        print(author.text)
