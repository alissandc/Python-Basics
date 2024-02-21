# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 05:52:24 2024

@author: Alissandra
"""
from pathlib import Path
import csv
from time import sleep
import win32com.client as client

csv_path = Path(r'C:\Users\Alissandra\PC\Downloads\Python Basics\Python-Basics\Outlook', 'people.csv')

template = "{}, please submit your time as soon as possible."
with open(csv_path, 'r', newline='') as f:
    reader = csv.reader(f)
    distro = [row for row in reader]

#list comprehension:
chunks = [distro[x:x+30] for x in range(0, len(distro), 30)]
outlook = client.Dispatch('Outlook.Application')
for chunk in chunks:
    for name, email in distro:
        message = outlook.CreateItem(0)
        message.To = email
        message.Subject = "Testing_01 Your time entry is past due!"
        message.Body = template.format(name)
        message.Save()
    sleep(60)