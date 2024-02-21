# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 20:21:23 2024

@author: Alissandra
"""

import win32com.client as client
outlook = client.Dispatch('Outlook.Application')
namespace = outlook.GetNameSpace('MAPI')
drafts = namespace.GetDefaultFolder(16)
inbox = namespace.GetDefaultFolder(6)
pyfolder = inbox.Folders['Python']
#print(pyfolder.Name)
#pyfolder = inbox.Folders[0]
#pyfolder = inbox.Folders.Item(1)
for folder in inbox.Folders:
    print("Inbox folder names: ", folder.Name)
print("Inbox folder count: ", inbox.Folders.Count)
print("Inbox folder name: ", inbox.Name)
print("Inbox folder description: ", inbox.Description)


#Created new folder
#inbox.Folders.Add('YTVideos')
#The following line assigns a description to the outlook folder YTVideos
inbox.Folders['YTVideos'].Description = "Messages related to my channel"

#prints the folder path of the inbox
print("Inbox folder path: ", inbox.FolderPath)

#prints the name of the parent folder
parent = pyfolder.Parent
print("name of the parent folder: ", parent.Name)

#gets the first mail in the inbox and prints the subject line
print("Subject of first email: ",inbox.Items[0].Subject)

#Creates a new folder in inbox, moves to python folder, then deletes the new folder
newFolder = inbox.Folders.Add('MyNewFolder')
newFolder.MoveTo(pyfolder)
newFolder.Delete()

#print the name of the accounts
for folder in namespace.folders:
    print("Account names: ", folder.Name)
    
#Navigate gmail account and index inbox folders in different ways:
gmail = namespace.Folders['alissandc@gmail.com']
print("gmail: ", gmail.Name)
gmail_inbox = gmail.folders['Inbox']
print(gmail_inbox.Name)
gmail_inbox = gmail.Folders[0]
print(gmail_inbox.Name)
gmail_inbox = gmail.Folders.Item(1)
print(gmail_inbox)
                                 