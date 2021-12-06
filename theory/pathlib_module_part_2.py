# https://realpython.com/python-pathlib/#operating-system-differences
import pathlib

# OPERATING SYSTEM DIFFERENCE

# Earlier, we noted that when we instantiated pathlib.Path, either a WindowsPath or a PosixPath object was returned.
# The kind of object will depend on the operating system you are using. This feature makes it fairly easy to write
# cross-platform compatible code. It is possible to ask for a WindowsPath or a PosixPath explicitly, but you will only
# be limiting your code to that system without any benefits. A concrete path like this can not be used on a different
# system:

# >>> pathlib.WindowsPath('test.md')
# NotImplementedError: cannot instantiate 'WindowsPath' on your system

# There might be times when you need a representation of a path without access to the underlying file system (in which
# case it could also make sense to represent a Windows path on a non-Windows system or vice versa). This can be done
# with PurePath objects. These objects support the operations discussed in the section on Path Components but not
# the methods that access the file system:

path = pathlib.PureWindowsPath(r'C:\Users\root\Projects\sandbox\theory\test.md')
assert path.name == 'test.md'
assert path.parent == pathlib.PureWindowsPath(r'C:\Users\root\Projects\sandbox\theory')
# >>> path.exists() --> AttributeError: 'PureWindowsPath' object has no attribute 'exists'

# You can directly instantiate PureWindowsPath or PurePosixPath on all systems. Instantiating PurePath will return
# one of these objects depending on the operating system you are using.

# PATH AS PROPER OBJECT

# The official documentation of pathlib is titled pathlib — Object-oriented filesystem paths.
# Independently of the operating system you are using, paths are represented in Posix style, with the forward slash
# as the path separator. On Windows, you will see something like this:

# >>> pathlib.Path(r'C:\Users\root\Projects\sandbox\theory\test.md')
# WindowsPath('C:/Users/root/Projects/sandbox/theory/test.md')

# Still, when a path is converted to a string, it will use the native form, for instance with backslashes on Windows:
assert str(pathlib.Path(
    r'C:\Users\root\Projects\sandbox\theory\test.md')) == r'C:\Users\root\Projects\sandbox\theory\test.md'
