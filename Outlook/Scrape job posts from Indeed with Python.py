# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 05:25:31 2024

@author: Alissandra
"""

"""Indeed Job Scraper
Create a general purpose job scraper for www.indeed.com
https://ph.indeed.com/jobs?q=work+from+home&l=Quezon+City&from=searchOnHP
"""

import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup


# def get_url(position, location):
#     """Generate a url from position and location"""
#     template = 'https://ph.indeed.com/jobs?q={}&l={}'
#     url = template.format(position, location)
#     return url

# url = get_url('work from home', 'Quezon City')

#Extract raw html
response = requests.get('https://ph.indeed.com/jobs?q=work+from+home&l=Quezon+City&from=searchOnHP')
print(response)
