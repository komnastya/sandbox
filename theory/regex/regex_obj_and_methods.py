import re
from re import match, search

# REGULAR EXPRESSIONS. PART V.
# MATCH OBJECT METHODS AND ATTRIBUTES.

# MATCH OBJECT METHODS

# As you’ve seen, most functions and methods in the re module return a match object when there’s a successful match.
# Because a match object is truthy, you can use it in a conditional.

# But match objects also contain quite a bit of handy information about the match. You’ve already seen some of it
# —the span= and match= data that the interpreter shows when it displays a match object. You can obtain much more
# from a match object using its methods and attributes.

# match_obj.group([<group1>, ...])
# Returns the specified captured group(s) from a match.

# For numbered groups, match.group(n) returns the nth group:
m = search(r'(\w+),(\w+),(\w+)', 'foo,bar,baz')
assert m.group(1) == "foo"
assert m.group(3) == "baz"

# Remember: Numbered captured groups are one-based, not zero-based.

# If you capture groups using (?P<name><regex>), then match_obj.group(<name>) returns the corresponding named group:
m = match(r'(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)', 'quux,corge,grault')
assert m.group('w1') == "quux"
assert m.group('w3') == "grault"

# With more than one argument, match_obj.group() returns a tuple of all the groups specified. A given group
# can appear multiple times, and you can specify any captured groups in any order:
m = search(r'(\w+),(\w+),(\w+)', 'foo,bar,baz')
assert m.group(1, 3) == ('foo', 'baz')
assert m.group(3, 3, 1, 1, 2, 2) == ('baz', 'baz', 'foo', 'foo', 'bar', 'bar')

m = match(r'(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)', 'quux,corge,grault')
assert m.group('w3', 'w1', 'w1', 'w2') == ('grault', 'quux', 'quux', 'corge')

# If you specify a group that’s out of range or nonexistent, then match_obj.group() raises an IndexError exception:
m = search(r'(\w+),(\w+),(\w+)', 'foo,bar,baz')
# assert m.group(4) -> IndexError: no such group

m = match(r'(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)', 'quux,corge,grault')
# assert m.group('foo') -> IndexError: no such group

# It’s possible for a regex in Python to match as a whole but to contain a group that doesn’t participate
# in the match. In that case, match_obj.group() returns None for the nonparticipating group. Consider this example:

m = search(r'(\w+),(\w+),(\w+)?', 'foo,bar,')
assert m.group() == "foo,bar,"
assert m.group(1, 2) == ('foo', 'bar')
assert m.group(3) is None
assert m.group() == "foo,bar,"
assert m.group(0) == "foo,bar,"
assert m.group() == m.group(0)

# match.__getitem__(<grp>)
# Returns a captured group from a match.

# match.__getitem__(<grp>) is identical to match.group(<grp>) and returns the single group specified by <grp>:
m = search(r'(\w+),(\w+),(\w+)', 'foo,bar,baz')
assert m.group(2) == "bar"
assert m.__getitem__(2) == "bar"
assert m.group(2) == m.__getitem__(2)

# .__getitem__() is one of a collection of methods in Python called magic methods. These are special methods that
# the interpreter calls when a Python statement contains specific corresponding syntactical elements.
# The particular syntax that .__getitem__() corresponds to is indexing with square brackets. For any object obj,
# whenever you use the expression obj[n], behind the scenes Python quietly translates it to a call to .__getitem__().

# As of Python version 3.6, the re module does implement .__getitem__() for match objects. The implementation is such
# that match.__getitem__(n) is the same as match.group(n).

# The result of all this is that, instead of calling match_obj.group() directly, you can access captured groups
# from a match object using square-bracket indexing syntax instead:

m = search(r'(\w+),(\w+),(\w+)', 'foo,bar,baz')
assert m.__getitem__(2) == "bar"
assert m[2] == "bar"

# This works with named captured groups as well:

m = match(r'foo,(?P<w1>\w+),(?P<w2>\w+),qux', 'foo,bar,baz,qux')
assert m.group('w2') == "baz"
assert m['w2'] == "baz"

# NB!: This is the example on syntaxis sugar, when we use m['w2'] instead of m.group('w2')


# match_obj.groups(default=None)
# Returns all captured groups from a match.
# match_obj.groups() returns a tuple of all captured groups:
m = search(r'(\w+),(\w+),(\w+)', 'foo,bar,baz')
assert m.groups() == ("foo", "bar", "baz")

# Compare:
assert m.group() == "foo,bar,baz"
assert m.group(0) == "foo,bar,baz"
assert m.group(1) == "foo"
assert m.group(2) == "bar"
assert m.group(3) == "baz"

# As you saw previously, when a group in a regex in Python doesn’t participate in the overall match, .group() returns
# None for that group. By default, .groups() does likewise.

# If you want .groups() to return something else in this situation, then you can use the default keyword argument:

m = search(r'(\w+),(\w+),(\w+)?', 'foo,bar,')
assert m.group() == "foo,bar,"
assert m.group(3) is None

assert m.groups() == ('foo', 'bar', None)
assert m.groups(default='something') == ('foo', 'bar', 'something')

# Here, the third (\w+) group doesn’t participate in the match because the question mark (?) metacharacter makes
# it optional, and the string 'foo,bar,' doesn’t contain a third sequence of word characters. By default, m.groups()
# returns None for the third group, you can see that specifying default='something' causes it to return
# the string 'something' instead.

# There isn’t any corresponding default keyword for .group(). It always returns None for nonparticipating groups.


# match_obj.groupdict(default=None)
# Returns a dictionary of named captured groups.

# match_obj.groupdict() returns a dictionary of all named groups captured with the (?P<name><regex>) metacharacter
# sequence. The dictionary keys are the group names and the dictionary values are the corresponding group values:

m = match(r'foo,(?P<w1>\w+),(?P<w2>\w+),qux', 'foo,bar,baz,qux')
assert m.groupdict() == {'w1': 'bar', 'w2': 'baz'}
assert m.groupdict()['w1'] == "bar"
assert m.groupdict()['w2'] == "baz"

# As with .groups(), for .groupdict() the default argument determines the return value for nonparticipating groups:
m = match(r'foo,(?P<w1>\w+),(?P<w2>\w+)?,qux', 'foo,bar,,qux')
assert m.groupdict() == {'w1': 'bar', 'w2': None}
assert m.groupdict(default='smth') == {'w1': 'bar', 'w2': 'smth'}

# match_obj.expand(<template>)
# Performs backreference substitutions from a match.
# match_obj.expand(<template>) returns the string that results from performing backreference substitution
# on <template> exactly as re.sub() would do:

m = search(r'(\w+),(\w+),(\w+)', 'foo,bar,baz')
assert m.group() == "foo,bar,baz"
assert m.groups() == ("foo", "bar", "baz")

assert m.expand(r'\2') == "bar"
assert m.expand(r'[\3] -> [\1]') == "[baz] -> [foo]"

m = search(r'(?P<num>\d+)', 'foo123qux')
assert m.group() == "123"
assert m.group(1) == "123"
assert m.expand(r'--- \g<num> ---') == "--- 123 ---"

# match_obj.start([<grp>])
# match_obj.end([<grp>])
# Return the starting and ending indices of the match.

# match_obj.start() returns the index in the search string where the match begins, and match_obj.end() returns the
# index immediately after where the match ends:

s = 'foo123bar456baz'
m = search('\d+', s)
assert m.group() == "123"
assert m.start() == 3
assert m.end() == 6

# When Python displays a match object, these are the values listed with the span= keyword. They behave like
# string-slicing values, so if you use them to slice the original search string, then you should get the
# matching substring:
assert s[m.start():m.end()] == "123"

# match_obj.start(<grp>) and match.end(<grp>)
# return the starting and ending indices of the substring matched by <grp>, which may be a numbered or named group:
s = "foo123bar456baz"
m = search(r'(\d+)\D*(?P<num>\d+)', s)
assert m.group(1) == "123"
assert m.start(1), m.end(1) == (3, 6)
assert s[m.start(1):m.end(1)] == "123"
assert m.group('num') == "456"
assert m.start('num'), m.end('num') == (9, 12)
assert s[m.start('num'):m.end('num')] == "456"

# If the specified group matches a null string, then .start() and .end() are equal:
m = search('foo(\d*)bar', 'foobar')
assert m[1] == ""
assert m.start(1), m.end(1) == (3, 3)
assert s[m.start(1):m.end(1)] == ""

# This makes sense if you remember that .start() and .end() act like slicing indices. Any string slice
# where the beginning and ending indices are equal will always be an empty string.

# A special case occurs when the regex contains a group that doesn’t participate in the match:
m = search(r'(\w+),(\w+),(\w+)?', 'foo,bar,')
assert m.group(3) is None
assert m.start(3), m.end(3) == (-1, -1)
# As you’ve seen previously, in this case the third group doesn’t participate. m.start(3) and m.end(3) aren’t
# really meaningful here, so they return -1.

# match.span([<grp>])
# Returns both the starting and ending indices of the match.

# match.span() returns both the starting and ending indices of the match as a tuple. If you specified <grp>,
# then the return tuple applies to the given group:

s = "foo123bar456baz"
m = search(r'(\d+)\D*(?P<num>\d+)', s)
assert m.group() == "123bar456"

assert m[0] == "123bar456"
assert m.span() == (3, 12)
assert m[1] == '123'
assert m.span(1) == (3, 6)
assert m['num'] == "456"
assert m.span('num') == (9, 12)

# The following are effectively equivalent:
# - match.span(<grp>)
# - (match.start(<grp>), match.end(<grp>))
# match.span() just provides a convenient way to obtain both match.start() and match.end() in one method call.

# MATCHED OBJECT ATTRIBUTES
# Like a compiled regular expression object, a match object also has several useful attributes available.

# match.pos
# match.endpos
# Contain the effective values of <pos> and <endpos> for the search.

# Remember that some methods, when invoked on a compiled regex, accept optional <pos> and <endpos> arguments
# that limit the search to a portion of the specified search string. These values are accessible from the match object
# with the .pos and .endpos attributes:

re_obj = re.compile(r'\d+')
m = re_obj.search('foo123bar', 2, 7)
assert m.group() == "123"
assert m.pos, m.endpos == (2, 7)

# If the <pos> and <endpos> arguments aren’t included in the call, either because they were omitted or because
# the function in question doesn’t accept them, then the .pos and .endpos attributes effectively
# indicate the start and end of the string:
re_obj = re.compile(r'\d+')
m = re_obj.search('foo123bar')
assert m.group() == "123"
assert m.pos == 0
assert m.endpos == 9

m = re.search(r'\d+', 'foo123bar')
assert m.group() == "123"
assert m.pos == 0
assert m.endpos == 9

# The re_obj.search() call above on line 242 could take <pos> and <endpos> arguments, but they aren’t specified.
# The re.search() call on line 246 can’t take them at all. In either case, m.pos and m.endpos are 0 and 9,
# the starting and ending indices of the search string 'foo123bar'.

# match.lastindex
# Contains the index of the last captured group.

# match.lastindex is equal to the integer index of the last captured group:
m = re.search(r'(\w+),(\w+),(\w+)', 'foo,bar,baz')
assert m.lastindex == 3
assert m[m.lastindex] == "baz"

# In cases where the regex contains potentially nonparticipating groups, this allows you to determine how many groups
# actually participated in the match:
m = re.search(r'(\w+),(\w+),(\w+)?', 'foo,bar,baz')
assert m.groups() == ('foo', 'bar', 'baz')
assert m.lastindex, m[m.lastindex] == (3, 'baz')

m = search(r'(\w+),(\w+),(\w+)?', 'foo,bar,')
assert m.groups() == ('foo', 'bar', None)
assert m.lastindex, m[m.lastindex] == (2, 'bar')

# There’s a subtle point to be aware of regarding .lastindex. It isn’t always the case that the last group to match
# is also the last group encountered syntactically. The Python documentation gives this example:

m = re.match('((a)(b))', 'ab')
assert m.groups() == ('ab', 'a', 'b')
assert m.lastindex == 1
assert m[m.lastindex] == "ab"

# The outermost group is ((a)(b)), which matches 'ab'. This is the first group the parser encounters, so it
# becomes group 1. But it’s also the last group to match, which is why m.lastindex is 1.

# The second and third groups the parser recognizes are (a) and (b). These are groups 2 and 3, but they match
# before group 1 does.

# match.lastgroup
# Contains the name of the last captured group.

# If the last captured group originates from the (?P<name><regex>) metacharacter sequence, then match.lastgroup
# returns the name of that group:
s = "foo123bar456baz"
m = search(r'(?P<n1>\d+)\D*(?P<n2>\d+)', s)
assert m.lastgroup == "n2"

# match.lastgroup returns None if the last captured group isn’t a named group:
s = "foo123bar456baz"
m = search(r'(\d+)\D*(\d+)', s)
assert m.groups() == ('123', '456')
assert m.lastgroup is None

m = search(r'\d+\D*\d+', s)
assert m.groups() == ()
assert m.lastgroup is None

# match_obj.re
# Contains the regular expression object for the match.

# match_obj.re contains the regular expression object that produced the match. This is the same object you’d
# get if you passed the regex to re.compile():

regex = r'(\w+),(\w+),(\w+)'
m1 = search(regex, 'foo,bar,baz')
assert m1.group() == "foo,bar,baz"
assert m1.re == re.compile('(\\w+),(\\w+),(\\w+)')

re_obj = re.compile(regex)
assert re_obj == re.compile('(\\w+),(\\w+),(\\w+)')
assert (re_obj is m1.re) is True

m2 = re_obj.search('qux,quux,corge')
assert m2.group() == "qux,quux,corge"
assert m2.re == re.compile('(\\w+),(\\w+),(\\w+)')
assert (m2.re is re_obj is m1.re) is True

# Once you have access to the regular expression object for the match, all of that object’s attributes
# are available as well:

assert m1.re.groups == 3
assert m1.re.pattern == '(\\w+),(\\w+),(\\w+)'
assert (m1.re.pattern == regex) is True
assert m1.re.flags == 32



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
