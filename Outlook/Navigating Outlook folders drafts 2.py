# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 21:03:48 2024

@author: Alissandra
"""

import win32com.client as client
outlook = client.Dispatch('Outlook.Application')
namespace = outlook.GetNameSpace('MAPI')
drafts = namespace.GetDefaultFolder(16)
print(drafts.Items.Count)
message = drafts.Items[0]
message = drafts.Items.Item(1)
message.SenderName
message.SenderEmailAddress
message.Subject
print(message.Body)
# message.Body = "Hey, there"
# print(message.Body)
# #message.Display()
# message.Save()
# message.Delete()
message = drafts.Items[0]
#Creates 10 copies of the message
# for x in range(10):
#     message.Copy()
for message in drafts.Items:
    print(message.Subject)

messages = list(drafts.Items)
print(len(messages))
messages = [item for item in drafts.Items if 'Izzy' in item.Subject]
print(len(messages))
for message in messages:
    message.Send()

