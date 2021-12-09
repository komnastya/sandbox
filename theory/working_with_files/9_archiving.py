# https://realpython.com/working-with-files-in-python/#archiving
import os
import shutil
import tarfile
import time
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

# CREATING NEW TAR ARCHIVE

files_to_archive = ['1_directory_listing.py', '2_getting_file_attributes.py']

#  Opening an archive in write mode('w') enables you to write new files to the archive. Any existing files in the
#  archive are deleted and a new archive is created:
with tarfile.open('new.tar', mode='w') as new_tar:
    for file in files_to_archive:
        new_tar.add(file)

# + theory
#   ...
#   new.tar (archive)
#       - 1_...
#       - 2_...

# After the archive is created and populated, the with context manager automatically closes it and saves it to the
# filesystem. The last three lines open the archive you just created and print out the names of the files contained
# in it:
members_name = []

with tarfile.open('new.tar', mode='r') as t:
    for member in t.getmembers():
        members_name.append(member.name)

assert members_name == ['1_directory_listing.py', '2_getting_file_attributes.py']

# To add new files to an existing archive, open the archive in append mode ('a'):
with tarfile.open('new.tar', 'a') as tar:
    tar.add('3_making_directories.py')

# + theory
#   ...
#   new.tar (archive)
#       - 1_...
#       - 2_...
#       - 3_...


# OPENING TAR ARCHIVES

# TAR files are uncompressed file archives like ZIP. They can be compressed using gzip, bzip2, and lzma compression
# methods. The TarFile class allows reading and writing of TAR archives.

tar = tarfile.TarFile('new.tar', 'r')

# Use the 'r', 'w' or 'a' modes to open an uncompressed TAR file for reading, writing, and appending, respectively.
# .open() defaults to 'r' mode. To read an uncompressed TAR file and retrieve the names of the files in it,
# use .getnames():
assert tar.getnames() == ['1_directory_listing.py', '2_getting_file_attributes.py', '3_making_directories.py']

# The metadata of each entry in the archive can be accessed using special attributes:
for entry in tar.getmembers():
    print()
    print(entry.name)
    print(' Modified:', time.ctime(entry.mtime))
    print(' Size    :', entry.size, 'bytes')

# In this example, you loop through the list of files returned by .getmembers() and print out each file’s attributes.
# The objects returned by .getmembers() have attributes that can be accessed programmatically such as the name, size,
# and last modified time of each of the files in the archive. After reading or writing to the archive, it must be
# closed to free up system resources.


# EXTRACTING FILES FROM A TAR ARCHIVE

# To extract a single file from a TAR archive, use extract(), passing in the filename:
tar.extract('1_directory_listing.py', path=r'.\new_folder')

# + theory
#   ...
#   new.tar (archive)
#       - 1_...
#       - 2_...
#       - 3_...
#   + new_folder
#       - 1_...

# To unpack or extract everything from the archive, use .extractall():
tar.extractall(path='tar_archive/')

# + theory
#   ...
#   new.tar (archive)
#       - 1_...
#       - 2_...
#       - 3_...
#   + new_folder
#       - 1_...
#   + tar_archive (folder)
#       - 1_...
#       - 2_...
#       - 3_...

# .extractall() has an optional path argument to specify where extracted files should go. Here, the archive is unpacked
# into the tar_archive directory.

# To extract a file object for reading or writing, use .extractfile(), which takes a filename or TarInfo object to
# extract as an argument. .extractfile() returns a file-like object that can be read and used:

f = tar.extractfile('1_directory_listing.py')
f.read()
tar.close()

# Opened archives should always be closed after they have been read or written to. To close an archive, call .close()
# on the archive file handle or use the with statement when creating tarfile objects to automatically close the archive
# when you’re done. This frees up system resources and writes any changes you made to the archive to the filesystem.

# Delete file and directory created in this example:
os.remove('new.tar')
shutil.rmtree('new_folder')
shutil.rmtree('tar_archive')

# WORKING WITH COMPRESSED ARCHIVES

# tarfile can also read and write TAR archives compressed using gzip, bzip2, and lzma compression. To read or write to
# a compressed archive, use tarfile.open(), passing in the appropriate mode for the compression type.

# For example, to read or write data to a TAR archive compressed using gzip, use the 'r:gz' or 'w:gz' modes
# respectively:

# >>> files = ['app.py', 'config.py', 'tests.py']
# >>> with tarfile.open('packages.tar.gz', mode='w:gz') as tar:
# ...     tar.add('app.py')
# ...     tar.add('config.py')
# ...     tar.add('tests.py')

# >>> with tarfile.open('packages.tar.gz', mode='r:gz') as t:
# ...     for member in t.getmembers():
# ...         print(member.name)
# app.py
# config.py
# tests.py

# The 'w:gz' mode opens the archive for gzip compressed writing and 'r:gz' opens the archive for gzip compressed
# reading. Opening compressed archives in append mode is not possible. To add files to a compressed archive, you have
# to create a new archive.


# AN EASIER WAY TO CREATING ARCHIVES
# https://realpython.com/working-with-files-in-python/#an-easier-way-of-creating-archives

# The Python Standard Library also supports creating TAR and ZIP archives using the high-level methods in the shutil
# module. The archiving utilities in shutil allow you to create, read, and extract ZIP and TAR archives. These utilities
# rely on the lower level tarfile and zipfile modules.

# shutil.make_archive() takes at least two arguments: the name of the archive and an archive format.

# By default, it compresses all the files in the current directory into the archive format specified in the format
# argument. You can pass in an optional root_dir argument to compress files in a different directory.
# .make_archive() supports the zip, tar, bztar, and gztar archive formats.

# shutil.make_archive(base_name, format, root_dir)
shutil.make_archive('archive/backup', 'zip', '.')

# This copies everything in archive/ and creates an archive called backup.zip in the filesystem and returns its name.
# To extract the archive, call .unpack_archive():

shutil.unpack_archive('archive/backup.zip', 'extract_dir/')

# Calling .unpack_archive() and passing in an archive name and destination directory extracts the contents of backup.tar
# into extract_dir/. TAR archives can be created and extracted in the same way.

# Delete directories created in this example:
shutil.rmtree('archive')
shutil.rmtree('extract_dir')
