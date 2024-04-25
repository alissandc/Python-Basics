# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 03:18:56 2024

@author: acayabyab
"""

# Python program to explain os.path.getmtime() method 
   
# importing os and time module 
import os
import time
import datetime
 
# Path
path = os.path.abspath('C:\\Users\\Downloads\\New Text Document.txt')
 
# Get the time of last
# modification of the specified
# path since the epoch
modification_time = os.path.getmtime(path)
print("Last modification time since the epoch:", modification_time)
 
# convert the time in
# seconds since epoch
# to local time
local_time = time.ctime(modification_time)
print("Last modification time(Local time):", local_time)

dt = datetime.datetime.fromtimestamp(modification_time)
print(dt)

xx = str(dt)
print(xx[0:5])
