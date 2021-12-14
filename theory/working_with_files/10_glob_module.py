import glob

# In Python, the glob module is used to retrieve files/pathnames matching a specified pattern.
# The pattern rules of glob follow standard Unix path expansion rules. It is also predicted that according to benchmarks
# it is faster than other methods to match pathnames in directories. With glob, we can also use wildcards ("*, ?,
# [ranges]) apart from exact string search to make path retrieval more simple and convenient.
import pathlib

print('Named explicitly:')
for name in glob.glob('./1_directory_listing.py'):
    print(name)

# Using '*' pattern
print('\nNamed with wildcard *:')
for name in glob.glob('./*'):
    print(name)

# Using '?' pattern
print('\nNamed with wildcard ?:')
for name in glob.glob('./data_??_backup.txt'):
    print(name)

# Using [0-9] pattern
print('\nNamed with wildcard ranges:')
for name in glob.glob('./[0-9]*.*'):
    print(name)

# We can use the function glob.glob() or glob.iglob() directly from glob module to retrieve paths recursively from
# inside the directories/files and subdirectories/subfiles.
# Syntax:
# glob.glob(pathname, *, recursive=False)
# glob.iglob(pathname, *, recursive=False)

# When recursive is set True “**” followed by path separator('./**/') will match any files or directories.

path = pathlib.Path(__file__).parent.parent

print("\nUsing recursive glob.glob(path, recursive=True)")
for file in glob.glob(f'{path}/**/*.txt', recursive=True):
    print(file)

# .iglob returns an iterator which will be printed simultaneously.
print("\nUsing glob.iglob()")
for filename in glob.iglob(f'{path}/**/*.md', recursive=True):
    print(filename)
