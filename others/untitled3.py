# -*- coding: utf-8 -*-
"""
Created on Thu May  9 02:39:34 2024

@author: acayabyab
"""

exlist = ['apple', 'red', 'apple', 'red', 'red', 'pear']

counts = dict()
for i in exlist:
  counts[i] = counts.get(i, 0) + 1

print(counts)