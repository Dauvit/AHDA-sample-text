#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 5, Example 5.
"""

# collocations

import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords

F_IN = 'Frankenstein.txt'

with open(F_IN, 'r', encoding='utf-8', newline='\n') as f_in:
    raw_text = f_in.read()
    tokens = nltk.word_tokenize(raw_text)
    bcf = nltk.BigramCollocationFinder.from_words(tokens)
    best_four = bcf.nbest(nltk.BigramAssocMeasures.likelihood_ratio, 4)
    print(best_four)
    print()
    stop_list = stopwords.words('english')
    filter_stops = lambda word: len(word) < 3 or word in stop_list
    bcf.apply_word_filter(filter_stops)
    best_four = bcf.nbest(nltk.BigramAssocMeasures.likelihood_ratio, 4)
    print(best_four)
