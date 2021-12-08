# https://realpython.com/working-with-files-in-python/#archiving
import os
import shutil
import zipfile

# ARCHIVING

#  The two most common archive types are ZIP and TAR. The Python programs you write can create, read, and extract
#  data from archives.


# READING ZIP FILES

# The zipfile module is a low level module that is part of the Python Standard Library. zipfile has functions that make
# it easy to open and extract ZIP files. To read the contents of a ZIP file, the first thing to do is to create a
# ZipFile object. ZipFile objects are similar to file objects created using open(). ZipFile is also a context manager
# and therefore supports the with statement:

with zipfile.ZipFile('data.zip', 'r') as zip_obj_example:
    pass

# Here, you create a ZipFile object, passing in the name of the ZIP file to open in read mode. After opening a ZIP file,
# information about the archive can be accessed through functions provided by the zipfile module. The data.zip archive
# in the example above was created from a directory named data that contains a total of 5 files and 1 subdirectory:

# To get a list of files in the archive, call namelist() on the ZipFile object:
zip_obj = zipfile.ZipFile('data.zip', 'r')
assert zip_obj.namelist() == ['file1.py', 'file2.py', 'file3.py', 'sub_dir/', 'sub_dir/bar.py', 'sub_dir/foo.py']

# .namelist() returns a list of names of the files and directories in the archive. To retrieve information about the
# files in the archive, use .getinfo():
bar_info = zip_obj.getinfo('sub_dir/bar.py')
assert bar_info.file_size == 0

# .getinfo() returns a ZipInfo object that stores information about a single member of the archive. To get information
# about a file in the archive, you pass its path as an argument to .getinfo(). Using getinfo(), you’re able to retrieve
# information about archive members such as the date the files were last modified, their compressed sizes, and their
# full filenames. Accessing .file_size retrieves the file’s original size in bytes.

# The following example shows how to retrieve more details about archived files in a Python REPL.

print(f'bar_info.filename is {bar_info.filename}')
print(f'bar_info.date_time is {bar_info.date_time}')
print(f'bar_info.compress_size is {bar_info.compress_size}')

# bar_info contains details about bar.py such as its size when compressed and its full path.

# The first line shows how to retrieve a file’s last modified date. The next line shows how to get the size of the
# file after compression. The last line shows the full path of bar.py in the archive.

# ZipFile supports the context manager protocol, which is why you’re able to use it with the with statement. Doing this
# automatically closes the ZipFile object after you’re done with it. Trying to open or extract files from a closed
# ZipFile object will result in an error.


# EXTRACTING ZIP ARCHIVES

# The zipfile module allows you to extract one or more files from ZIP archives through .extract() and .extractall().

# These methods extract files to the current directory by default. They both take an optional path parameter that allows
# you to specify a different directory to extract files to. If the directory does not exist, it is automatically
# created. To extract files from the archive, do the following:

data_zip = zipfile.ZipFile('data.zip', 'r')  # open data.zip in read mode

# Extract a single file to current directory:
data_zip.extract('file1.py')  # call .extract() to extract file1.py from data_zip .extract() returns the full file
# path of the extracted file. Since there’s no path specified, .extract() extracts file1.py to the current directory.

# Extract all files into a different directory named 'extract_dir'
data_zip.extractall(path='extract_dir/')  # extract the entire archive into the zip_extract directory. .extractall()
# creates the extract_dir and extracts the contents of data.zip into it.

data_zip.close()  # close the ZIP archive

# Delete files extracted in this example:
os.remove('file1.py')
shutil.rmtree('extract_dir')


# EXTRACTING DATA FROM PASSWORD PROTECTED ARCHIVES

with zipfile.ZipFile('secret.zip', 'r') as pwd_zip:
    # Extract from a password protected archive
    pwd_zip.extractall(path='secret_dir', pwd=b'1234')

# This opens the secret.zip archive in read mode. A password is supplied to .extractall(), and the archive contents
# are extracted to secret_dir. The archive is closed automatically after the extraction is complete thanks to the
# with statement.

# Delete directory extracted in this example:
shutil.rmtree('secret_dir')


# CREATING NEW ZIP ARCHIVES

file_list = ['1_directory_listing.py', '2_getting_file_attributes.py', '3_making_directories.py',
             '4_filename_pattern_matching.py', '5_traversing_directories_and_processing_files.py',
             '6_make_temporary_files_and_directories.py', '7_delete_files_and_directories.py',
             '8_copy_move_rename_files_and_dirs.py']

# To create a new ZIP archive, you open a ZipFile object in write mode (w) and add the files you want to archive:
with zipfile.ZipFile('new.zip', 'w') as new_zip:
    for name in file_list:
        new_zip.write(name)

# In the example, new_zip is opened in write mode and each file in file_list is added to the archive. When the with
# statement suite is finished, new_zip is closed. Opening a ZIP file in write mode erases the contents of the archive
# and creates a new archive.

# To add files to an existing archive, open a ZipFile object in append mode and then add the files:
with zipfile.ZipFile('new.zip', 'a') as new_zip:
    new_zip.write('data_03_backup.txt')

# Here, you open the new.zip archive you created in the previous example in append mode. Opening the ZipFile object
# in append mode allows you to add new files to the ZIP file without deleting its current contents. After adding files
# to the ZIP file, the with statement goes out of context and closes the ZIP file.

# Delete the archive created in this example:
os.remove('new.zip')
