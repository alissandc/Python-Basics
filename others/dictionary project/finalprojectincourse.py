# -*- coding: utf-8 -*-
"""
Created on Thu May  9 02:43:55 2024

@author: acayabyab
"""

#!/usr/bin/env python3

import re
# import operator
import os
import csv

error_dict = {}
info_per_user = {}
error_per_user = {}
parentheses_user = r'\(([^)]+)\)'
infonumber = r'\[#\d+\]'
#initialize error dictionary as a nested dictionary
error_dict = {0: {'Error': 'none', 'Count': 0}, 
              1: {'Error': 'The ticket was modified while updating', 'Count': 0}}
# print(error_dict)
# print(error_dict[0]['Error'])
# print(error_dict[0]['Count'])
error_dict[0]['Count'] = 20
print(error_dict)

# def readingfile(logfile):
#   with open(logfile) as file:
#     for line in file:
#       if len(line) > 0:
#           if re.search(r"ticky: INFO ([\w ]*) ", line):
#             reg = re.search(r"ticky: INFO ", line)
#             reg_user = re.search(parentheses_user, line)
#             reg_info = re.search(infonumber, line)
#             regend = reg.end()
#             reg_user_start = reg_user.start()
#             reg_info_start = reg_info.start()
#             info = line[regend:reg_info_start].strip()
#             usern = reg_user.group(1)
#             if usern in info_per_user:
#                 info_per_user[usern] += 1
#             else:
#                 info_per_user[usern] = 1
#           elif re.search(r"ticky: ERROR ([\w ]*) ", line):
#             reg = re.search(r"ticky: ERROR ", line)
#             reg_user = re.search(parentheses_user, line)
#             regend = reg.end()
#             reg_user_start = reg_user.start()
#             errorline = line[regend:reg_user_start].strip()
#             if errorline in error_dict:
#                 error_dict[errorline] += 1
#             else:
#                 error_dict[errorline] = 1
#             usern = reg_user.group(1)
#             if usern in error_per_user:
#                 error_per_user[usern] += 1
#             else:
#                 error_per_user[usern] = 1

# def createcsvforerror(errordictcsv):
#     sortederrordictcsv = dict(sorted(errordictcsv.items(), key=lambda x: x[1], reverse=True))
#     column_names = ["Error", "Count"]
#     with open('dict.csv', 'w') as csv_file:  
#         writer = csv.writer(csv_file)
#         writer.writerow(column_names)
#         for key, value in sortederrordictcsv.items():
#            writer.writerow([key, value])

# def createcsvforusers(dict1, dict2):
#     userdicts = dict1, dict2
#     keys = ["Username", "INFO", "ERROR"]
#     #keys = ["name", "username", "department"]
#     with open('by_department.csv', 'w') as by_department:
#         writer = csv.DictWriter(by_department)
#         writer.writerow(keys)
#         writer.writerows(userdicts)


# sysl = os.path.abspath('C:\\Users\\acayabyab\\Downloads\\pytest\syslog.log')
# readingfile(sysl)
# createcsvforerror(error_dict)
# createcsvforusers(info_per_user, error_per_user)
# print(os.getcwd())