# https://realpython.com/working-with-files-in-python/#making-directories

import os
import pathlib
import shutil

# MAKING DIRECTORIES

# Sooner or later, the programs you write will have to create directories in order to store data in them.
# os and pathlib include functions for creating directories:

# os.mkdir()                Creates a single subdirectory
# os.makedirs()	            Creates multiple directories, including intermediate directories
# pathlib.Path.mkdir()	    Creates single or multiple directories

# CREATING A SINGLE DIRECTORY

# To create a single directory, pass a path to the directory as a parameter to os.mkdir():

example_directory = 'example_directory/'
os.mkdir(example_directory)

# If a directory already exists, os.mkdir() raises FileExistsError.
# Alternatively, you can create a directory using pathlib:
example_directory_2 = pathlib.Path('example_directory_2')
example_directory_2.mkdir()

# If the path already exists, mkdir() raises a FileExistsError.
# To avoid errors like this, catch the error when it happens and let your user know:

try:
    example_directory_2.mkdir()
except FileExistsError as exc:
    pass

# Alternatively, you can ignore the FileExistsError by passing the exist_ok=True argument to .mkdir().
# This will not raise an error if the directory already exists:
example_directory_2.mkdir(exist_ok=True)

os.rmdir(example_directory)
os.rmdir(example_directory_2)  # delete the created directories

# CREATE MULTIPLE DIRECTORIES

# os.makedirs() is similar to os.mkdir(). The difference between the two is that not only can os.makedirs() create
# individual directories, it can also be used to create directory trees. In other words, it can create any necessary
# intermediate folders in order to ensure a full path exists.
# In order to create a group of directories like 2021/12/07, all you have to do is the following:

today = '2021/12/07'
os.makedirs(today)
shutil.rmtree('2021')  # delete non-empty directory

# .makedirs() creates directories with default permissions. If you need to create directories with different
# permissions call .makedirs() and pass in the mode you would like the directories to be created in:
os.makedirs(today, mode=0o770)
# This creates the 2021/12/07 directory structure and gives the owner and group users read, write, and execute
# permissions. The default mode is 0o777, and the file permission bits of existing parent directories are not changed.

shutil.rmtree('2021')  # delete non-empty directory

# An alternative way to create directories is to use .mkdir() from pathlib.Path:
p = pathlib.Path(today)
p.mkdir(parents=True)
# Passing parents=True to Path.mkdir() makes it create the directory 07 and any parent directories necessary to make
# the path valid.

# By default, os.makedirs() and Path.mkdir() raise an OSError if the target directory already exists. This behavior c
# an be overridden (as of Python 3.2) by passing exist_ok=True as a keyword argument when calling each function.
p.mkdir(exist_ok=True)

shutil.rmtree('2021')  # delete non-empty directory
