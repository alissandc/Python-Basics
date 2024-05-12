# -*- coding: utf-8 -*-
"""
Created on Fri May  3 21:39:19 2024

@author: acayabyab
"""

import re

regexp = r"\d+_"

origstr = "2024-05-02 17-01-15_New Property List - MONTHLY_CARDINAL"
result = re.search(regexp, origstr)
position = result.end()
newname = origstr[position:]
print(newname)