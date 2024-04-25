#The new_directory function creates a new directory inside the current working directory, then creates a new empty file inside the new directory, and returns the list of files in that directory.

import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    os.mkdir(os.path.join(os.getcwd(), directory))

  # Create the new file inside of the new directory
  os.chdir(directory)
  with open (filename, "w") as file:
    file.write("this is a new file")
    pass

  # Return the list of files in the new directory
  return os.listdir(os.getcwd())

print(new_directory("PythonPrograms", "script.py"))