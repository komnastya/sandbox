# https://realpython.com/working-with-files-in-python/#getting-a-directory-listing
import os
import pathlib

# GETTING A DIRECTORY LISTING

# The built-in os module has a number of useful functions that can be used to list directory contents and filter the
# results. To get a list of all the files and folders in a particular directory in the filesystem, use os.listdir() in
# legacy versions of Python or os.scandir() in Python 3.x.
# os.scandir() is the preferred method to use if you also want to get file and directory properties such as file size
# and modification date.

# DIRECTORY LISTING IN MODERN PYTHON VERSION

# os.scandir() and pathlib.Path() are used for directory listing in modern versions of python.
# os.scandir() returns an iterator as opposed to a list when called:
path_example = os.scandir(pathlib.Path.cwd())  # ScandirIterator class object

# The ScandirIterator points to all the entries in the current directory. You can loop over the contents of the
# iterator and print out the filenames:
files_in_dir = []
path = pathlib.Path.cwd()
with os.scandir(path) as entries:
    for entry in entries:
        files_in_dir.append(entry.name)

# Here, os.scandir() is used in conjunction with the with statement because it supports the context manager protocol.
# Using a context manager closes the iterator and frees up acquired resources automatically after the iterator has
# been exhausted.

# Another way to get a directory listing is to use the pathlib module:
files_in_dir2 = []
for entry in path.iterdir():
    files_in_dir2.append(entry.name)

assert files_in_dir == files_in_dir2  # lists of all files in 'theory' folder

# pathlib.Path() objects have an .iterdir() method for creating an iterator of all files and folders in a directory.
# Each entry yielded by .iterdir() contains information about the file or directory such as its name and file
# attributes. pathlib is a great addition to Python that provides an object oriented interface to the filesystem.

# pathlib offers a set of classes featuring most of the common operations on paths in an easy, object-oriented way.
# Using pathlib is more if not equally efficient as using the functions in os. Another benefit of using pathlib over
# os is that it reduces the number of imports you need to make to manipulate filesystem paths.

# pathlib.Path() offers much of the file and path handling functionality found in os and shutil, and it’s methods are
# more efficient than some found in these modules. We will discuss how to get file properties shortly.

# Here are the directory-listing functions again:

# os.listdir()	            Returns a list of all files and folders in a directory
# os.scandir()	            Returns an iterator of all the objects in a directory including file attribute information
# pathlib.Path.iterdir()	Returns an iterator of all the objects in a directory including file attribute information

# These functions return a list of everything in the directory, including subdirectories. This might not always be
# the behavior you want. The next section will show you how to filter the results from a directory listing.

# LISTING ALL FILES IN A DIRECTORY:

# To filter out directories and only list files from a directory listing produced by os.listdir(), use os.path:
# List all files in a directory using os.listdir

# List all files in a directory using os.listdir
files_one = []
for entry in os.listdir(path):
    if os.path.isfile(os.path.join(path, entry)):
        files_one.append(entry)

# files_one contains only files, not folders

# An easier way to list files in a directory is to use os.scandir() or pathlib.Path():
# # List all files in a directory using scandir()
files_two = []
with os.scandir(path) as entries:
    for entry in entries:
        if entry.is_file():
            files_two.append(entry.name)

assert files_one == files_two  # both objects contain the lists of file inside the theory folder

# Using os.scandir() has the advantage of looking cleaner and being easier to understand than using os.listdir(),
# even though it is one line of code longer. Calling entry.is_file() on each item in the ScandirIterator returns True
# if the object is a file.

# Here’s how to list files in a directory using pathlib.Path():
files_three = []
# this statement points to the 'theory' folder itself
files_in_basepath = path.iterdir()
for item in files_in_basepath:
    if item.is_file():
        files_three.append(item.name)

assert files_three == files_two
assert files_three == files_one

# The code above can be made more concise if you combine the for loop and the if statement into a single generator
# expression. The modified version looks like this:
files_four = [entry.name for entry in path.iterdir() if entry.is_file()]

assert files_four == files_one
assert files_four == files_two
assert files_four == files_three

# LISTING SUBDERICTORIES:

# To list subdirectories instead of files, use one of the methods below. Here’s how to use os.listdir() and os.path():

directories = []
for entry in os.listdir(path):
    if os.path.isdir(os.path.join(path, entry)):
        directories.append(entry)

# Manipulating filesystem paths this way can quickly become cumbersome when you have multiple calls to os.path.join().
# Here’s how to use os.scandir():
# # List all subdirectories using scandir():
directories_two = []
with os.scandir(path) as entries:
    for entry in entries:
        if entry.is_dir():
            directories_two.append(entry.name)

assert directories == directories_two  # both objects contain the list of folders inside the 'theory' folder

# As in the file listing example, here you call .is_dir() on each entry returned by os.scandir(). If the entry is a
# directory, .is_dir() returns True, and the directory’s name is appended to the list.
# Here’s how to use pathlib.Path():
directories_three = []
for entry in path.iterdir():
    if entry.is_dir():
        directories_three.append(entry.name)

assert directories_three == directories
assert directories_three == directories_two
