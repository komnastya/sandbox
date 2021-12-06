# https://realpython.com/python-pathlib/
import pathlib

# CREATING PATH

# There are a few different ways of creating a path. First of all, there are classmethods like .cwd() (Current Working
# Directory) and .home() (your user’s home directory):
first_path = pathlib.Path.cwd()
assert str(first_path) == 'C:\\Users\\root\\Projects\\sandbox\\theory'

# A path can also be explicitly created from its string representation:
second_path = pathlib.Path(r'C:\Users\root\Projects\sandbox\theory')
assert str(second_path) == 'C:\\Users\\root\\Projects\\sandbox\\theory'

# A little tip for dealing with Windows paths: on Windows, the path separator is a backslash, \. However, in many
# contexts, backslash is also used as an escape character in order to represent non-printable characters. To avoid
# problems, use raw string literals to represent Windows paths. These are string literals that have an r prepended to
# them. In raw string literals the \ represents a literal backslash: r'C:\Users'.

# A third way to construct a path is to join the parts of the path using the special operator /. The forward slash
# operator is used independently of the actual path separator on the platform:
third_path = pathlib.Path.home() / 'Projects' / 'sandbox' / 'theory'
assert str(third_path) == 'C:\\Users\\root\\Projects\\sandbox\\theory'

# The / can join several paths or a mix of paths and strings (as above) as long as there is at least one Path object.
# If you do not like the special / notation, you can do the same thing with the .joinpath() method:
fourth_path = pathlib.Path.home().joinpath('Projects', 'sandbox', 'theory')
assert str(fourth_path) == 'C:\\Users\\root\\Projects\\sandbox\\theory'


# READING AND WRITING FILES

# Traditionally, the way to read or write a file in Python has been to use the built-in open() function. This is still
# true as the open() function can use Path objects directly. The following example finds all headers in a Markdown file
# and prints them:
path = pathlib.Path.cwd() / 'test.md'
with open(path, mode='r') as fid:
    headers = [line.strip() for line in fid if line.startswith('#')]
assert headers == ['# Header 1', '## Header 2', '### Header 3', '#### Header 4']

# An equivalent alternative is to call .open() on the Path object:
with path.open(mode='r') as fid:
    headers = [line.strip() for line in fid if line.startswith('#')]
assert headers == ['# Header 1', '## Header 2', '### Header 3', '#### Header 4']

# In fact, Path.open() is calling the built-in open() behind the scenes. Which option you use is mainly a matter of
# taste.
# For simple reading and writing of files, there are a couple of convenience methods in the pathlib library:
# .read_text(): open the path in text mode and return the contents as a string.
# .read_bytes(): open the path in binary/bytes mode and return the contents as a bytestring.
# .write_text(): open the path and write string data to it.
# .write_bytes(): open the path in binary/bytes mode and write data to it.

# Each of these methods handles the opening and closing of the file, making them trivial to use, for instance:
path = pathlib.Path.cwd() / 'test.md'
print('Reading the text: ', path.read_text())

# Paths can also be specified as simple file names, in which case they are interpreted relative to the current working
# directory. The following example is equivalent to the previous one:
text = pathlib.Path('test.md').read_text()
print('\nThe same text: ', text)

# The .resolve() method will find the full path. Below, we confirm that the current working directory is used for simple
# file names:
path = pathlib.Path('test.md')
assert str(path) == 'test.md'
assert path.resolve().parent == pathlib.Path.cwd()  # C:\Users\root\Projects\sandbox\theory
assert path.parent != pathlib.Path.cwd()

# PICKING OUT COMPONENTS OF THE PATH

path_of_the_file = pathlib.Path('test.md')
# The different parts of a path are conveniently available as properties. Basic examples include:

# .name: the file name without any directory
assert path_of_the_file.name == 'test.md'

# .parent: the directory containing the file, or the parent directory if path is a directory:
# path_of_the_file.parent => .

# .stem: the file name without the suffix
assert path_of_the_file.stem == 'test'

# .suffix: the file extension
assert path_of_the_file.suffix == '.md'

# .anchor: the part of the path before the directories
# path_of_the_file.anchor => \

# Note that .parent returns a new Path object, whereas the other properties return strings. This means for instance
# that .parent can be chained as in the last example or even combined with / to create completely new paths:
new_path = path.parent.parent / ('new' + path.suffix)
assert str(new_path) == 'new.md'

assert str(path.absolute()) == r'C:\Users\root\Projects\sandbox\theory\test.md'

# MOVING AND DELETING FILES

# Through pathlib, you also have access to basic file system level operations like moving, updating, and even deleting
# files. For the most part, these methods do not give a warning or wait for confirmation before information or files
# are lost. Be careful when using these methods.

# To move a file, use .replace(). Note that if the destination already exists, .replace() will overwrite it.
# Unfortunately, pathlib does not explicitly support safe moving of files. To avoid possibly overwriting the destination
# path, the simplest is to test whether the destination exists before replacing:

# if not destination.exists():
#     source.replace(destination)

# However, this does leave the door open for a possible race condition. Another process may add a file at the
# destination path between the execution of the if statement and the .replace() method. If that is a concern, a safer
# way is to open the destination path for exclusive creation and explicitly copy the source data:

# with destination.open(mode='xb') as fid:
#     fid.write(source.read_bytes())

# When you are renaming files, useful methods might be .with_name() and .with_suffix(). They both return the original
# path but with the name or the suffix replaced, respectively. For instance:

assert str(path) == 'test.md'
assert str(path.with_suffix('.py')) == 'test.py'
# path.replace(path.with_suffix('.py')) -> change the file format
