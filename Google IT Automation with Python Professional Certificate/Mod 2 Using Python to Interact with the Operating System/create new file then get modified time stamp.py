import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(os.path.join(os.getcwd(), filename), "w") as file:
    file.write("comments")
  timestamp = os.path.getmtime(os.path.join(os.getcwd(), filename))
  # Convert the timestamp into a readable format, then into a string
  dt = datetime.datetime.fromtimestamp(timestamp)
  strdt = str(dt)
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{}".format(strdt[0:10]))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd