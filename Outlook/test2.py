# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 21:23:56 2024

@author: Alissandra
"""

from pathlib import Path
new_path = Path('.')
#print(new_path)
cake_path = Path(r'C:\Users\Alissandra\OneDrive - ateneo.edu\Pictures', 'fashioncat-lede-1300x1950.jpg')
folder = Path(r'C:\Users\Alissandra\OneDrive - ateneo.edu\Pictures')
cert_path = Path(r'C:\Users\Alissandra\OneDrive - ateneo.edu\Pictures','missing npc.jpg')
for pics in folder.glob('*.jpg'):
    print(pics)
#print(list(folder.glob('*.jpg')))