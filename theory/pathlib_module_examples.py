# https://realpython.com/python-pathlib/#examples
import collections
import pathlib
from datetime import datetime

# EXAMPLE 1: COUNTING FILES

# There are a few different ways to list many files. The simplest is the .iterdir() method, which iterates over all
# files in the given directory. The following example combines .iterdir() with the collections.Counter class to count
# how many files there are of each filetype in the current directory:

collection = collections.Counter(p.suffix for p in pathlib.Path.cwd().iterdir())
# collection -> Counter({'.py': 27, '': 4, '.txt': 1, '.md': 1})

# More flexible file listings can be created with the methods .glob() and .rglob() (recursive glob). For instance,
# pathlib.Path.cwd().glob('*.txt') returns all files with a .txt suffix in the current directory. The following only
# counts filetypes starting with p:

only_p = collections.Counter(p.suffix for p in pathlib.Path.cwd().glob('*.p*'))
# only_p -> Counter({'.py': 27, '': 1})


# EXAMPLE 2: DISPLAY A DIRECTORY TREE

# The next example defines a function, tree(), that will print a visual tree representing the file hierarchy, rooted
# at a given directory. Here, we want to list subdirectories as well, so we use the .rglob() method:

def tree(directory):
    print(f'+ {directory}')
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = '    ' * depth
        print(f'{spacer}+ {path.name}')

print('Example 2: displayed a directory tree.')
tree(pathlib.Path.cwd())

# Note that we need to know how far away from the root directory a file is located. To do this, we first use
# .relative_to() to represent a path relative to the root directory. Then, we count the number of directories
# (using the .parts property) in the representation. When run, this function creates a visual tree.


# EXAMPLE 3: FIND THE LAST MODIFIED FILE

# The .iterdir(), .glob(), and .rglob() methods are great fits for generator expressions and list comprehensions. To
# find the file in a directory that was last modified, you can use the .stat() method to get information about the
# underlying files. For instance, .stat().st_mtime gives the time of last modification of a file:

directory = pathlib.Path.cwd()
time, file_path = max((f.stat().st_mtime, f) for f in directory.iterdir())
print('\nExample 3: Find the last modified file: ')
print(datetime.fromtimestamp(time), file_path)


# EXAMPLE 4: CREATE A UNIQUE FILE NAME

# The last example will show how to construct a unique numbered file name based on a template. First, specify a pattern
# for the file name, with room for a counter. Then, check the existence of the file path created by joining a directory
# and the file name (with a value for the counter). If it already exists, increase the counter and try again:

def unique_path(directory, name_pattern):
    counter = 0
    while True:
        counter += 1
        path = directory / name_pattern.format(counter)
        if not path.exists():
            return path

path = unique_path(pathlib.Path.cwd(), 'test{:03d}.txt')

# If the directory already contains the files test001.txt and test002.txt, the above code will set path to test003.txt.
print('\nExample 4: Create a unique file name: ', path)
