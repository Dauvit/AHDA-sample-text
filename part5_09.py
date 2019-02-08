#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 5, Example 9.
"""

# Parts Of Speech tagging

import pprint

import nltk

sentence = "He spoke of the spoke on his bicycle."
tokens = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(tokens)
pprint.pprint(pos_tags)
