# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 19:52:34 2024

@author: Alissandra
"""

from pathlib import Path
import csv
csv_path = Path(r'C:\Users\Alissandra\PC\Downloads\Python Basics\Python-Basics\Outlook', 'people.csv')

with open(csv_path, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    distro = [row for row in reader]
    print(len(distro))
    
#chunks = [distro[x:x+30] for x in range(0, len(distro), 30)]

chunks = []
for x in range(0, len(distro), 30):
    chunk = distro[x:x+30]
    chunks.append(chunk)

for c in chunks:
    print('Count of items: ', c)