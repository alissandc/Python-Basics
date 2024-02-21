#!/usr/bin/env python
# coding: utf-8

# Adding Excel content to Outlook Email

# In[58]:


import os
import win32com.client as client
from PIL import ImageGrab


# Copy and Save Excel Range as Image

# In[59]:


workbook_path = os.getcwd() + '\\heatmap.xlsx'


# In[60]:


excel = client.Dispatch('Excel.Application')


# In[61]:


wb = excel.Workbooks.Open(workbook_path)


# In[62]:


sheet = wb.Sheets.Item(1)


# In[63]:


sheet = wb.Sheets[0]


# In[64]:


sheet = wb.Sheets['Sheet1']


# In[65]:


excel.visible = 1


# In[66]:


copyrange = sheet.Range('A1:M11')


# In[67]:


copyrange.CopyPicture(Appearance=1, Format=2)


# #Appearance=1, how it looks on the screen. if 2, how it looks when printed
# #Format=2, copied in a bitmap format such as bmp or jpeg

# In[68]:


ImageGrab.grabclipboard().save('paste.png')


# In[69]:


excel.Quit()


# Create Outlook email and insert Excel content

# In[70]:


image_path = os.getcwd() + '\\paste.png'


# In[71]:


outlook = client.Dispatch('Outlook.Application')


# In[72]:


message = outlook.CreateItem(0)


# In[73]:


message.To = "someone@email.com"


# In[74]:


message.Subject = "Please review!"


# In[75]:


image = message.Attachments.Add(image_path)


# In[76]:


image.PropertyAccessor.SetProperty("http://schemas.microsoft.com/mapi/proptag/0x3712001F", "paste-img")


# In[77]:


html_body = """
    <div>
        Please review the following report and respond with your feedback.<br><br>
    </div>
    <div>
        <img src="cid:paste-img" width=50%></img>
    </div>
"""


# In[78]:


message.HTMLBody = html_body


# In[79]:


message.Display()


# In[80]:


message.Save()


# or message.Send() if you want to send!
