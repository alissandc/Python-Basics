# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 22:00:58 2024

@author: acayabyab
"""

import os
import re
qtrname = r"Q1 2024"

os.chdir('C:\\Users\\acayabyab\\OneDrive - RealPage\\Documents\\OpsMerchant Top 100 quarterly\\company automation\\Result')

print(os.getcwd())

lst = os.listdir()
number_of_files = len(lst)
#print(number_of_files)

for file in os.listdir():
    name, ext = os.path.splitext(file)
    result = re.search(qtrname, file)
    start = result.start()
    suppliername = file[0:start-1]
    newname = f"{suppliername} {qtrname}_pmc.xlsx"
    os.rename(file, newname)