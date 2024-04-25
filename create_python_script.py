# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 03:40:59 2024

@author: acayabyab
"""
import os
print(os.getcwd())

path = os.path.abspath('C:\\Users\\Documents\\Python Scripts')

os.chdir(path)

print(os.getcwd())

def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(os.path.join(os.getcwd(), filename), "w") as file:
    file.write(comments)
  filesize = os.path.getsize(os.path.join(os.getcwd(), filename))
  return(filesize)

print(create_python_script("program.py"))
