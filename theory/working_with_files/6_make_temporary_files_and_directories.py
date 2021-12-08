# https://realpython.com/working-with-files-in-python/#making-temporary-files-and-directories
import os
from tempfile import TemporaryDirectory, TemporaryFile

# MAKING TEMPORARY FILES AND DIRECTORIES

# Python provides a handy module for creating temporary files and directories called tempfile.

# tempfile can be used to open and store data temporarily in a file or directory while your program is running.
# tempfile handles the deletion of the temporary files when your program is done with them.

# CREATE TEMPORARY FILE.

# The first step is to import TemporaryFile from the tempfile module. Next, create a file like object using the
# TemporaryFile() method by calling it and passing the mode you want to open the file in. This will create and open
# a file that can be used as a temporary storage area:
fp = TemporaryFile('w+t')
fp.write('Hello universe!')

# Go back to the beginning and read data from file:
fp.seek(0)
data = fp.read()

# Once the file is closed, it will be deleted from the filesystem:
fp.close()

# In the example above, the mode is 'w+t', which makes tempfile create a temporary text file in write mode. There is
# no need to give the temporary file a filename since it will be destroyed after the script is done running.

# If you need to name the temporary files produced using tempfile, use tempfile.NamedTemporaryFile().

# The temporary files and directories created using tempfile are stored in a special system directory for storing
# temporary files. Python searches a standard list of directories to find one that the user can create files in.

# .TemporaryFile() is also a context manager so it can be used in conjunction with the with statement. Using a context
# manager takes care of closing and deleting the file automatically after it has been read:
with TemporaryFile('w+t') as fp:
    fp.write('Hello universe!')
    fp.seek(0)
    fp.read()

# File is now closed and removed.

# This creates a temporary file and reads data from it. As soon as the file’s contents are read, the temporary file is
# closed and deleted from the file system.

# CREATE TEMPORARY DIRECTORY

# tempfile can also be used to create temporary directories. Let’s look at how you can do this using
# tempfile.TemporaryDirectory():

with TemporaryDirectory() as tmpdir:
    print('Created temporary directory ', tmpdir)
    print(os.path.exists(tmpdir))

# Directory contents have been removed

print(tmpdir)
print(os.path.exists(tmpdir))

# Calling tempfile.TemporaryDirectory() creates a temporary directory in the file system and returns an object
# representing this directory. In the example above, the directory is created using a context manager, and the name of
# the directory is stored in tmpdir. The second line prints out the name of the temporary directory, and
# os.path.exists(tmpdir) confirms if the directory was actually created in the file system.

# After the context manager goes out of context, the temporary directory is deleted and a call to os.path.exists(tmpdir)
# returns False, which means that the directory was successfully deleted.
