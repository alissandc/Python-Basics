# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 22:32:33 2024

@author: acayabyab
"""

import re
qtrname = r"Q1 2024"
filename = "Alliance Distributors & Services LLC Q1 2024 company"
result = re.search(qtrname, filename)
print(result)
print(result.start())
start = result.start()
print(result.group())
print(filename[0:start-1])
suppliername = filename[0:start-1]
newname = f"{suppliername} {qtrname}_pmc.xlsx"
print(newname)
