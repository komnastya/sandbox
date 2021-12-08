# https://realpython.com/working-with-files-in-python/#deleting-files-and-directories
import os
import pathlib

# DELETING FILES AND DIRECTORIES

# You can delete single files, directories, and entire directory trees using the methods found in the os, shutil, and
# pathlib modules.

# os.remove()           	Deletes a file and does not delete directories
# os.unlink()	            Is identical to os.remove() and deletes a single file
# pathlib.Path.unlink()	    Deletes a file and cannot delete directories
# os.rmdir()	            Deletes an empty directory
# pathlib.Path.rmdir()	    Deletes an empty directory
# shutil.rmtree()	        Deletes entire directory tree and can be used to delete non-empty directories

# DELETING FILES IN PYTHON

# To delete a single file, use pathlib.Path.unlink(), os.remove(). or os.unlink().

# os.remove() and os.unlink() are semantically identical. To delete a file using os.remove(), do the following:
import shutil

data_file = open('data.txt', 'x')  # create a new empty file
data_file.close()
path = '.\data.txt'
os.remove(path)

# Deleting a file using os.unlink() is similar to how you do it using os.remove():
data_file_2 = open('data2.txt', 'w')
data_file_2.close()
path_2 = '.\data2.txt'
os.unlink(path_2)

# Calling .unlink() or .remove() on a file deletes the file from the filesystem. These two functions will throw an
# OSError if the path passed to them points to a directory instead of a file. To avoid this, you can either check that
# what you’re trying to delete is actually a file and only delete it if it is, or you can use exception handling to
# handle the OSError:

home = '.\home'
os.mkdir(home)

data_file_3 = open('home/data3.txt', 'w')
data_file_3.close()

path_3 = '.\home\data3.txt'

# If the file exists, delete it
if os.path.isfile(path_3):
    os.remove(path_3)
else:
    print(f'Error: {path_3} is not valid name')

# os.path.isfile() checks whether data_file is actually a file. If it is, it is deleted by the call to os.remove().
# If data_file points to a folder, an error message is printed to the console.

# The following example shows how to use exception handling to handle errors when deleting files:
try:
    os.remove(path_3)
except OSError as e:
    print(f'Error: {path_3} : {e.strerror}')

# The code above attempts to delete the file. If data3 doesn't actually exists, the FileNotFoundError(OSError) that is
# thrown is handled in the except clause, and an error message is printed to the console. The error message that gets
# printed out is formatted using Python f-strings.

# Finally, you can also use pathlib.Path.unlink() to delete files:
data_file_4 = open('home/data4.txt', 'w')
data_file_4.close()

path_4 = pathlib.Path.cwd() / 'home' / 'data4.txt'
try:
    path_4.unlink()
except IsADirectoryError as e:
    print(f'Error: {path_4} : {e.strerror}')

# This creates a Path object called path_4 that points to a file. Calling .remove() on path_4 will delete home/data4.txt.
# If path_4 points to a directory, an IsADirectoryError is raised. It is worth noting that the Python program above
# has the same permissions as the user running it. If the user does not have permission to delete the file, a
# PermissionError is raised.

# DELETING DIRECTORIES

# The standard library offers the following functions for deleting directories:
# os.rmdir()	            Deletes an empty directory
# pathlib.Path.rmdir()	    Deletes an empty directory
# shutil.rmtree()	        Deletes entire directory tree and can be used to delete non-empty directories

# To delete a single directory or folder, use os.rmdir() or pathlib.rmdir(). These two functions only work if the
# directory you’re trying to delete is empty. If the directory isn’t empty, an OSError is raised. Here is how to delete
# a folder:

try:
    os.rmdir(home)
except OSError as e:
    print(f'Error: {home} : {e.strerror}')

# Here, the home directory is deleted by passing its path to os.rmdir(). If the directory isn’t empty, an error message
# is printed to the screen: # OSError: [Errno 39] Directory not empty: 'home'

# Alternatively, you can use pathlib to delete directories:
sandbox = pathlib.Path.cwd() / 'sandbox'
sandbox.mkdir()

try:
    sandbox.rmdir()
except OSError as e:
    print(f'Error: {sandbox} : {e.strerror}')

# Here, you create a Path object that points to the directory to be deleted. Calling .rmdir() on the Path object will
# delete it if it is empty.


# DELETING ENTIRE DIRECTORY TREE

# To delete non-empty directories and entire directory trees, Python offers shutil.rmtree():

box = pathlib.Path('box/examples/1')
box.mkdir(parents=True)

box_2 = 'box2/examples/01'
os.makedirs(box_2)

try:
    shutil.rmtree('box')
    shutil.rmtree('box2')
except OSError as e:
    print(f'Error: {box} : {e.strerror}')
