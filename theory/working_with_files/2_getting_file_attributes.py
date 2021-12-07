# https://realpython.com/working-with-files-in-python/#getting-file-attributes
import os
import pathlib
from datetime import datetime

# GETTING FILE ATTRIBUTES

# Python makes retrieving file attributes such as file size and modified times easy. This is done through os.stat(),
# os.scandir(), or pathlib.Path().

# os.scandir() and pathlib.Path() retrieve a directory listing with file attributes combined. This can be potentially
# more efficient than using os.listdir() to list files and then getting file attribute information for each file.

# The examples below show how to get the time the files in my_directory/ were last modified. The output is in seconds:
path = pathlib.Path.cwd()
dir_info = []

with os.scandir(path) as dir_contents:
    for entry in dir_contents:
        info = entry.stat()
        dir_info.append(info.st_mtime)

# os.scandir() returns a ScandirIterator object.
# Each entry in a ScandirIterator object has a .stat() method that retrieves information about the file or directory
# it points to.
# .stat() provides information such as file size and the time of last modification.
# In the example above, the code appends the st_mtime attribute, which is the time the content of the file was last
# modified.

# The pathlib module has corresponding methods for retrieving file information that give the same results:
dir_info_two = []
for entry in path.iterdir():
    info = entry.stat()
    dir_info_two.append(info.st_mtime)

assert dir_info == dir_info_two


# In the example above, the code loops through the object returned by .iterdir() and retrieves file attributes through
# a .stat() call for each file in the directory list. The st_mtime attribute returns a float value that represents
# seconds since the epoch. To convert the values returned by st_mtime for display purposes, you could write a helper
# function to convert the seconds into a datetime object:

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date


modified_time = []  # list of tuples, where first item is file name and the second one is the time when it was modified
# last time
with os.scandir(path) as dir_contents:
    for entry in dir_contents:
        if entry.is_file():
            info = entry.stat()
            modified_time.append((entry.name, convert_date(info.st_mtime)))

# This will first get a list of files in my_directory and their attributes and then call convert_date() to convert
# each file’s last modified time into a human readable form. convert_date() makes use of .strftime() to convert the
# time in seconds into a string.
