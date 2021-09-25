import re
from re import I, search

# COMPILED REGEX OBJECTS IN PYTHON. PART IV.

# The re module supports the capability to precompile a regex in Python into a regular expression object
# that can be repeatedly used later.

# re.compile(<regex>, flags=0)
# Compiles a regex into a regular expression object.

# re.compile(<regex>) compiles <regex> and returns the corresponding regular expression object. If you include
# a <flags> value, then the corresponding flags apply to any searches performed with the object.

# There are two ways to use a compiled regular expression object. You can specify it as the first argument to the
# re module functions in place of <regex>:

# re_obj = re.compile(<regex>, <flags>)
# result = re.search(re_obj, <string>)

# You can also invoke a method directly from a regular expression object:
# re_obj = re.compile(<regex>, <flags>)
# result = re_obj.search(<string>)

# Both of the examples above are equivalent to this:
# result = re.search(<regex>, <string>, <flags>)

# Here’s one of the examples you saw previously, recast using a compiled regular expression object:

assert search(r'(\d+)', 'foo123bar').group() == '123'

re_obj = re.compile(r'(\d+)')
assert search(re_obj, 'foo123bar').group() == "123"

assert re_obj.search('foo123bar').group() == "123"

# Here’s another, which also uses the IGNORECASE flag:

r1 = search('ba[rz]', 'FOOBARBAZ', flags=I)

re_obj = re.compile('ba[rz]', flags=re.I)
r2 = search(re_obj, 'FOOBARBAZ')
r3 = re_obj.search('FOOBARBAZ')

assert r1.group() == "BAR"
assert r2.group() == "BAR"
assert r3.group() == "BAR"

# There are a couple of possible advantages.
# If you use a particular regex in your Python code frequently, then precompiling allows you to separate out the
# regex definition from its uses. This enhances modularity. Consider this example:

s1, s2, s3, s4 = 'foo.bar', 'foo123bar', 'baz99', 'qux & grault'

assert search('\d+', s1) is None
assert search('\d+', s2).group() == "123"
assert search('\d+', s3).group() == "99"
assert search('\d+', s4) is None

# Here, the regex \d+ appears several times. If, in the course of maintaining this code, you decide you need a
# different regex, then you’ll need to change it in each location. That’s not so bad in this small example because
# the uses are close to one another. But in a larger application, they might be widely scattered and difficult
# to track down.

# The following is more modular and more maintainable:

s1, s2, s3, s4 = 'foo.bar', 'foo123bar', 'baz99', 'qux & grault'
re_obj = re.compile('\d+')

assert re_obj.search(s1) is None
assert re_obj.search(s2).group() == "123"
assert re_obj.search(s3).group() == "99"
assert re_obj.search(s4) is None

# Then again, you can achieve similar modularity without precompiling by using variable assignment:

s1, s2, s3, s4 = 'foo.bar', 'foo123bar', 'baz99', 'qux & grault'
regex = '\d+'

assert search(regex, s1) is None
assert search(regex, s2).group() == "123"
assert search(regex, s3).group() == "99"
assert search(regex, s4) is None


# REGULAR EXPRESSION OBJECT METHODS
# A compiled regular expression object re_obj supports the following methods:

# re_obj.search(<string>[, <pos>[, <endpos>]])
# re_obj.match(<string>[, <pos>[, <endpos>]])
# re_obj.fullmatch(<string>[, <pos>[, <endpos>]])
# re_obj.findall(<string>[, <pos>[, <endpos>]])
# re_obj.finditer(<string>[, <pos>[, <endpos>]])

# These all behave the same way as the corresponding re functions that you’ve already encountered, with the
# exception that they also support the optional <pos> and <endpos> parameters. If these are present, then the search
# only applies to the portion of <string> indicated by <pos> and <endpos>, which act the same way as indices
# in slice notation:

re_obj = re.compile(r'\d+')
s = "foo123barbaz"

assert re_obj.search(s).group() == "123"
assert s[6:9] == "bar"
assert re_obj.search(s, 6, 9) is None

# In the above example, the regex is \d+, a sequence of digit characters. The .search() on line 103 searches all of s,
# so there’s a match. On line 105, the <pos> and <endpos> parameters effectively restrict the search to the
# substring starting with character 6 and going up to but not including character 9 (the substring 'bar'),
# which doesn’t contain any digits.

# If you specify <pos> but omit <endpos>, then the search applies to the substring from <pos> to the end of the string.

# Note that anchors such as caret (^) and dollar sign ($) still refer to the start and end of the entire string,
# not the substring determined by <pos> and <endpos>:

re_obj = re.compile('^bar')
s = "foobarbaz"
assert s[3:] == "barbaz"
assert re_obj.search(s, 3) is None

# Here, even though 'bar' does occur at the start of the substring beginning at character 3, it isn’t at the start
# of the entire string, so the caret (^) anchor fails to match.

# The following methods are available for a compiled regular expression object re_obj as well:
# re_obj.split(<string>, maxsplit=0)
# re_obj.sub(<repl>, <string>, count=0)
# re_obj.subn(<repl>, <string>, count=0)
# These also behave analogously to the corresponding re functions, but they don’t support the <pos> and
# <endpos> parameters.

# REGULAR EXPRESSION OBJECT ATTRIBUTES
# The re module defines several useful attributes for a compiled regular expression object.

# re_obj.flags
# Any <flags> that are in effect for the regex

# re_obj.groups
# The number of capturing groups in the regex

# re_obj.groupindex
# A dictionary mapping each symbolic group name defined by the (?P<name>)
# construct (if any) to the corresponding group number

# re_obj.pattern
# The <regex> pattern that produced this object

# The code below demonstrates some uses of these attributes:
re_obj = re.compile(r'(?m)(\w+),(\w+)', re.I)
assert re_obj.flags == 42 # WHY???
# >>> re.I|re.M|re.UNICODE
# <RegexFlag.UNICODE|MULTILINE|IGNORECASE: 42>

assert re_obj.groups == 2
assert re_obj.pattern == "(?m)(\\w+),(\\w+)"

re_obj = re.compile(r'(?P<w1>\d+),(?P<w2>\d+)')
assert re_obj.groupindex == {'w1': 1, 'w2': 2}
assert re_obj.groupindex['w1'] == 1
assert re_obj.groupindex['w2'] == 2

# You can also invoke any of the methods defined for a compiled regular expression object on it:
m = re.search(r'(\w+),(\w+),(\w+)', 'foo,bar,baz')
assert m.re == re.compile('(\\w+),(\\w+),(\\w+)')
assert m.re.match('quux,corge,grault').group() == "quux,corge,grault"

# Here, .match() is invoked on m.re to perform another search using the same regex but on a different search string.

# match.string
# Contains the search string for a match.

# match.string contains the search string that is the target of the match:
m = search(r'(\w+),(\w+),(\w+)', 'foo,bar,baz')
assert m.string == "foo,bar,baz"

re_obj = re.compile(r'(\w+),(\w+),(\w+)')
m = re_obj.search('foo,bar,baz')
assert m.string == "foo,bar,baz"

# As you can see from the example, the .string attribute is available when the match object derives from a
# compiled regular expression object as well.
