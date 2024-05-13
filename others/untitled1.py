
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 22:00:58 2024

@author: acayabyab
"""

import os
import re
#regex pattern:
regexp = r".xlsx"

os.chdir('C:\\Users\\acayabyab\\OneDrive - RealPage\\Documents\\Monthly scorecard data\\property list')

print(os.getcwd())

lst = os.listdir()
number_of_files = len(lst)
print(number_of_files)

for file in os.listdir():
    name, ext = os.path.splitext(file)
    result = re.search(regexp, file)
    lastposition = result.start()
    format_name = file[:lastposition]
    newname = f"{format_name}.xlsx"
    os.rename(file, newname)