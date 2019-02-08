#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python for AHDA.

Part 1, Example 9.
"""

# Deduplication of a list

rhyme = ['Peter', 'Piper', 'picked', 'a', 'piece', 'of', 'pickled', 'pepper', 'A', 'piece', 'of', 'pickled', 'pepper', 'Peter', 'Piper', 'picked']
deduplicated_rhyme = set(rhyme)
print(deduplicated_rhyme)
