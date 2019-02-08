#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 5, Example 10.
"""

# Named Entity Recognition

import nltk
nltk.download('max_ent_chunker')
nltk.download('words')

print()

sentence = "Francesca is working at The Open University in Britain."
tokens = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(tokens)
print(nltk.ne_chunk(pos_tags))
print()
# as a one liner if you prefer
# print(nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sentence))))
