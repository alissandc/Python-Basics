#The create_python_script function creates a new python script in the current working directory, adds the line of comments to it declared  by the 'comments' variable, and returns the size of the new file

import os
def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(os.path.join(os.getcwd(), filename), "w") as file:
    file.write(comments)
  filesize = os.path.getsize(os.path.join(os.getcwd(), filename))
  return(filesize)

print(create_python_script("program.py"))