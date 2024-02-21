# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 21:45:14 2024

@author: Alissandra
"""

import win32com.client as client
outlook = client.Dispatch('Outlook.Application')
namespace = outlook.GetNameSpace('MAPI')
account = namespace.Folders('alissandc@gmail.com')
inbox = account.Folders('Inbox')
# inbox.Name
# inbox.Parent.Name
# inbox.Items.Count

#1_Finds email addresses and moves to folder
# yt_mails = [message for message in inbox.Items if message.SenderEmailAddress.endswith('citi.com')]
# yt_folder = inbox.Folders('yt_folder')
# for message in yt_mails:
#     print(message)
#     #message.move(yt_folder)

#2_Finds messages that contain deal and moves to junk folder
# junk_messages = [message for message in inbox.Items if 'deal' in message.Body.lower()]
# len(junk_messages)
# for message in junk_messages:
#     print(message.SenderEmailAddress)
# for message in junk_messages:
#     print(message.Subject)
# junk_stuff = inbox.Folders.Add('JunkStuff')
# for message in junk_messages:
#     message.move(junk_stuff)

#3_Creates a function then searches the term and outputs a csv file
# #recursion - function that calls itself
def mail_body_search(term, folder):
    """Recursively search all folders for email containing search term"""
    relevant_messages = [(message, message.Parent.Name) for message in folder.Items if term in message.Body.lower()]
    
    #check for subfolders (base case)
    subfolder_count = folder.Folders.Count
    
    #search all subfolders
    if subfolder_count > 0:
        for subfolder in folder.Folders:
            relevant_messages.extend(mail_body_search(term, subfolder))
    
    return relevant_messages

# search for python in my account folder
results = mail_body_search('shaolin.online', account)
print(len(results))

# for message in results:
#     message.delete()

#save results to csv
import csv
with open('search_results.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['ParentFolder', 'Subject'])
    for message, parent in results:
        writer.writerow([parent, message.Subject])
    