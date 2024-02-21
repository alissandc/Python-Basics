# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 05:52:24 2024

@author: Alissandra
"""

import win32com.client as client
distro = []
for _ in range(1567):
    distro.append('alissa_lopez542@outlook.com')
    
chunks = []
for x in range(0, len(distro), 500):
    chunk = distro[x:x+500]
    chunks.append(chunk)
    

for c in chunks:
    print('Count of items: ', len(c))

outlook = client.Dispatch('Outlook.Application')
for recipients in chunks:
    message = outlook.CreateItem(0)
    message.To = ":".join(recipients)
    message.Subject = "Missing time alert!"
    message.Body = "Please submit your time as soon as possible!"
    message.Save()