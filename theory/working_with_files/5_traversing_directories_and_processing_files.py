# https://realpython.com/working-with-files-in-python/#traversing-directories-and-processing-files
import os

# TRAVERSING DIRECTORIES AND PROCESSING THE FILES

# os.walk() is used to generate filename in a directory tree by walking the tree either top-down or bottom-up.
# os.walk() defaults to traversing directories in a top-down manner.

# os.walk() returns three values on each iteration of the loop:
# The name of the current folder
# A list of folders in the current folder
# A list of files in the current folder

all_files = {}  # dictionary, which contain all_files files map to the folder name, so {folder_name: [files]}
for current_folder, inside_folders, inside_files in os.walk('.'):
    current_files = []
    for file_name in inside_files:
        current_files.append(file_name)
    all_files[current_folder] = current_files

# To traverse the directory tree in a bottom-up manner, pass in a topdown=False keyword argument to os.walk():
all_files_2 = {}
for current_folder, inside_folders, inside_files in os.walk('.', topdown=False):
    current_files = []
    for file_name in inside_files:
        current_files.append(file_name)
    all_files_2[current_folder] = current_files

# Passing the topdown=False argument will make os.walk() print out the files it finds in the subdirectories first. If
# there are not subdirectories in the folder, there is the same order.
assert all_files == all_files_2

# With topdown=false parameter the program started by listing the contents of the subdirectories before listing the
# contents of the root directory. This is very useful in situations where you want to recursively delete files and
# directories. By default, os.walk does not walk down into symbolic links that resolve to directories. This behavior can
# be overridden by calling it with a followlinks=True argument.
