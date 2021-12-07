# https://realpython.com/working-with-files-in-python/#filename-pattern-matching
import fnmatch
import glob
import os
import pathlib

# FILENAME PATTERN MATCHING

# After getting a list of files in a directory using one of the methods above, you will most probably want to search
# for files that match a particular pattern.

# These are the methods and functions available to you:

# endswith() and startswith() string methods
# fnmatch.fnmatch()
# glob.glob()
# pathlib.Path.glob()

# startswith()	                        Tests if a string starts with a specified pattern and returns True or False
# endswith()	                        Tests if a string ends with a specified pattern and returns True or False
# fnmatch.fnmatch(filename, pattern)	Tests whether the filename matches the pattern and returns True or False
# glob.glob()	                        Returns a list of filenames that match a pattern from current directory
# pathlib.Path.glob()	                Finds patterns in path names and returns a generator object

# USING STRINGS METHODS

# Python has several built-in methods for modifying and manipulating strings. Two of these methods, .startswith() and
# .endswith(), are useful when you’re searching for patterns in filenames. To do this, first get a directory listing
# and then iterate over it:

theory_folder = pathlib.Path.home() / 'Projects' / 'sandbox' / 'theory'

txt_files_in_folder = []
for f_name in theory_folder.iterdir():
    if f_name.name.endswith('.txt'):
        txt_files_in_folder.append(f_name.name)

assert txt_files_in_folder == ['data_01_backup.txt', 'data_02_backup.txt', 'names.txt']

# The code above finds all the files in theory/, iterates over them and uses .endswith() to print out the
# filenames that have the .txt file extension.

# SIMPLE FILENAME PATTERN MATCHING using FNMATCH

# String methods are limited in their matching abilities. fnmatch has more advanced functions and methods for pattern
# matching. We will consider fnmatch.fnmatch(), a function that supports the use of wildcards such as * and ? to match
# filenames. For example, in order to find all .md files in a directory using fnmatch, you would do the following:

markdown_file_in_folder = []
for f_name in os.listdir(theory_folder):
    if fnmatch.fnmatch(f_name, '*.md'):
        markdown_file_in_folder.append(f_name)

assert markdown_file_in_folder == ['test.md']
# This iterates over the list of files in theory directory and uses .fnmatch() to perform a wildcard search for files
# that have the .md extension.

# MORE ADVANCED PATTERN MATCHING

# Let’s suppose you want to find .txt files that meet certain criteria. For example, you could be only interested in
# finding .txt files that contain the word data, a number between a set of underscores, and the word 'backup' in their
# filename. Something similar to data_01_backup, data_02_backup, or data_03_backup.
# It's possible to do using the fnmatch():

data_backup_files = []
for f_name in os.listdir(theory_folder):
    if fnmatch.fnmatch(f_name, 'data_*_backup.txt'):
        data_backup_files.append(f_name)

assert data_backup_files == ['data_01_backup.txt', 'data_02_backup.txt']

# Here, you find only the names of files that match the data_*_backup.txt pattern. The asterisk in the pattern will
# match any character, so running this will find all text files whose filenames start with the word 'data' and end in
# 'backup.txt'.

# FILENAME PATTERN MATCHING using GLOB

# .glob() in the glob module works just like fnmatch.fnmatch(), but unlike fnmatch.fnmatch(), it treats files beginning
# with a period (.) as special.

# Here’s an example of how to use glob to search for all Python (.py) source files in the current directory:
all_python_files = glob.glob('*.py')  # lists of all .py files in 'working_with_filed' folder
# glob.glob('*.py') searches for all files that have the .py extension in the current directory and returns them as a
# list.
# glob also supports shell-style wildcards to match patterns:
backup_files = glob.glob('*[1-9]*.txt')

assert backup_files == ['data_03_backup.txt']

# glob makes it easy to search for files recursively in subdirectories too:
# for file in glob.iglob('**/*.py', recursive=True):
#      print(file)
# This example makes use of glob.iglob() to search for .py files in the current directory and subdirectories. Passing
# recursive=True as an argument to .iglob() makes it search for .py files in the current directory and any
# subdirectories. The difference between glob.iglob() and glob.glob() is that .iglob() returns an ITERATOR instead of
# a list.

#  pathlib contains similar methods for making flexible file listings. The example below shows how you can use
#  .Path.glob() to list file types that start with the letter p:
files_with_dir_in_name = []
p = pathlib.Path('.')
for name in p.glob('*dir*.py'):
    files_with_dir_in_name.append(name.name)

assert files_with_dir_in_name == ['directory_listing.py', 'making_directories.py']

# Calling p.glob('*dir*.py') returns a generator object that points to all python files in the current directory that
# contain dir in their name.

# Path.glob() is similar to os.glob() discussed above. As you can see, pathlib combines many of the best features of
# the os, os.path, and glob modules into one single module, which makes it a joy to use.
