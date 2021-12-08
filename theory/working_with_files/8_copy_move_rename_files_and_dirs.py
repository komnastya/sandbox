# https://realpython.com/working-with-files-in-python/#copying-moving-and-renaming-files-and-directories
import os
import pathlib
import shutil

# COPYING, MOVING, AND RENAMES FILES AND DIRECTORIES

# Python ships with the shutil module. shutil is short for shell utilities. It provides a number of high-level
# operations on files to support copying, archiving, and removal of files and directories.

# COPYING FILES IN PYTHON

# shutil offers a couple of functions for copying files. The most commonly used functions are shutil.copy() and
# shutil.copy2(). To copy a file from one location to another using shutil.copy(), do the following:

example_box_path = 'example_box'
os.mkdir(example_box_path)  # create 'example_box' directory

# + theory
#   ...
#   + example_box_directory

example_file = open('example_file.txt', 'w')
example_file.close()  # create 'example_file.txt' in 'theory' directory

# + theory
#   ...
#   + example_box_directory
#   example_file.txt

src = 'example_file.txt'
dst = 'example_box'
shutil.copy(src, dst)  # copy example_file from the 'theory' directory to the 'example_box' directory (without metadata)

# + theory
#   ...
#   + example_box_directory
#       example_file.txt (copy)
#   example_file.txt

# shutil.copy(src, dst) will copy the file src to the location specified in dst. If dst is a file, the contents of that
# file are replaced with the contents of src. If dst is a directory, then src will be copied into that directory.
# shutil.copy() only copies the file’s contents and the file’s permissions.
# Other metadata like the file’s creation and modification times are not preserved.

os.remove(r'example_box\example_file.txt')  # delete example_file from example_box directory

# + theory
#   ...
#   + example_box_directory
#   example_file.txt

# To preserve all file metadata when copying, use shutil.copy2():
shutil.copy2(src, dst)  # copy file to the example_box directory with metadata (last access time, permission bits, last
# modification time, and flags).

# + theory
#   ...
#   + example_box_directory
#       example_file.txt (copy)
#   example_file.txt

# COPYING DIRECTORY

# While shutil.copy() only copies a single file, shutil.copytree() will copy an entire directory and everything
# contained in it. shutil.copytree(src, dest) takes two arguments: a source directory and the destination directory
# where files and folders will be copied to.

data_file = open('example_box/data.txt', 'w')
data_file.close()

os.mkdir('example_box/inside_box')

# + theory
#   ...
#   + example_box_directory
#       + inside_box_directory
#       data.txt
#       example_file.txt (copy)
#   example_file.txt

# We add data.txt file and inside_box to the example_box directory created in previous example.

# Here’s an example of how to copy the contents of one directory to a different location:

shutil.copytree('example_box', 'example_box_backup')

# + theory
#   ...
#   + example_box_directory
#       + inside_box_directory
#       data.txt
#       example_file.txt
#   + example_box_backup_directory
#       + inside_box_directory
#       data.txt
#       example_file.txt
#   example_file.txt

# In this example, .copytree() copies the contents of example_box to a new location example_box_backup and returns the
# destination directory. The destination directory must not already exist. It will be created as well as missing parent
# directories. shutil.copytree() is a good way to back up your files.

# MOVING FILE AND DIRECTORIES

# To move a file or directory to another location, use shutil.move(src, dst).
# src is the file or directory to be moved and dst is the destination:
shutil.move('example_box_backup/data.txt', 'example_box_backup/inside_box')  # move data.txt file from
# example_box_backup to inside_box
shutil.move('example_box_backup/example_file.txt', 'example_box_backup/inside_box/')  # -- // --
shutil.move('example_box_backup/', 'example_box/')  # move example_box_backup directory to example_box directory

# + theory
#   ...
#   + example_box_directory
#      + example_box_backup_directory
#           + inside_box_directory
#               data.txt
#               example_file.txt
#       + inside_box_directory
#       data.txt
#       example_file.txt
#   example_file.txt

# shutil.move('example_box_backup/', 'example_box') moves example_box_backup into examples_box if example_box exists.
# If example_box does not exist, example_box_backup will be renamed to example_box.

# RENAMING FILES AND DIRECTORIES

# Python includes os.rename(src, dst) for renaming files and directories:
os.rename('example_box', 'box')
os.rename('example_file.txt', 'example.txt')

# Another way to rename files or directories is to use rename() from the pathlib module:
file_name = pathlib.Path.cwd() / 'example.txt'
file_name.rename('txt_file_example.txt')

# To rename files using pathlib, you first create a pathlib.Path() object that contains a path to the file you want to
# replace. The next step is to call rename() on the path object and pass a new filename for the file or directory
# you’re renaming.

# + theory
#   ...
#   + box_directory
#      + example_box_backup_directory
#           + inside_box_directory
#               data.txt
#               example_file.txt
#       + inside_box_directory
#       data.txt
#       example_file.txt
#   txt_file_example.txt

# Delete box directory and example.txt which have been in previous examples:
shutil.rmtree('box')
os.remove('txt_file_example.txt')
