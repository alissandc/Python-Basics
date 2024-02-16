# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 05:38:12 2024

@author: Alissandra
"""

import win32com.client as client
from pathlib import Path
outlook = client.Dispatch("Outlook.Application")
message = outlook.CreateItem(0)
message.Display()
message.To = "hoarders2@gmail.com"
message.Subject = "Happy Birthday"
html_body = """
    <div>
        <h1 style="font-family: 'Lucida Handwriting'; font-size: 56; font-weight: bold; color: #9eac9c;">
            Happy Birthday!!
        </h1>
        <span style="font-family: 'Lucida Sans'; font-size: 28; color: #8d395c;">
            {}, wishing you all the best on your birthday!!
        </span>
    </div><br>
    <div>
        <img src="https://chelsweets.com/wp-content/uploads/2022/11/recipe-card-penguin-cake-closer-735x980.jpg" width=50%>
    </div>

"""
message.HTMLBody = html_body
message.HTMLBody = html_body.format("Richard")