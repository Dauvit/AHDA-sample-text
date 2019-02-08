#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 2, Example 8.
"""

# Unzip and read an XML file usefully - actually .docx

import zipfile
from xml.etree.ElementTree import XML


WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
PARA = WORD_NAMESPACE + 'p'
TEXT = WORD_NAMESPACE + 't'

DOCX_IN = 'Frankenstein_25.docx'
TXT_OUT = 'Frankenstein_25_converted_from_docx.txt'


with zipfile.ZipFile(DOCX_IN) as f_zip:
    xml_content = f_zip.read('word/document.xml')
    tree = XML(xml_content)

paragraphs = []
for paragraph in tree.iter(PARA):
    texts = [node.text
             for node in paragraph.iter(TEXT)
             if node.text]
    if texts:
        paragraphs.append(''.join(texts))

with open(TXT_OUT, 'w', encoding='utf-8', newline='\n') as f_out:
    f_out.write('\n\n'.join(paragraphs))
