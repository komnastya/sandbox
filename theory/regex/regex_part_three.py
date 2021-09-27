from re import IGNORECASE, MULTILINE, escape, findall, finditer, fullmatch, match, search, split, sub, subn

# REGULAR EXPRESSION. PART III.
# re MODULE FUNCTIONS

# In addition to re.search(), the re module contains several other functions to help you perform regex-related tasks.

# Note: You saw in the previous tutorial that re.search() can take an optional <flags> argument, which specifies
# flags that modify parsing behavior. All the functions shown below, with the exception of re.escape(),
# support the <flags> argument in the same way.

# You can specify <flags> as either a positional argument or a keyword argument:
# re.search(<regex>, <string>, <flags>)
# re.search(<regex>, <string>, flags=<flags>)

# The default for <flags> is always 0, which indicates no special modification of matching behavior. Remember
# from the discussion of flags in the previous tutorial that the re.UNICODE flag is always set by default.

# The available regex functions in the Python re module fall into the following three categories:

# 1. Searching functions
# 2. Substitution functions
# 3. Utility functions


# 1. SEARCHING FUNCTIONS

# re.search(<regex>, <string>, flags=0)
# Scans a string for a regex match.
# The function returns a match object if it finds a match and None otherwise.
assert search(r'(\d+)', 'foo123bar').group() == "123"
assert search(r'[a-z]+', '123FOO456', flags=IGNORECASE).group() == 'FOO'
assert search(r'\d+', 'foo.bar') is None

# re.match(<regex>, <string>, flags=0)
# Looks for a regex match at the beginning of a string.

# This is identical to re.search(), except that re.search() returns a match if <regex> matches anywhere in <string>,
# whereas re.match() returns a match only if <regex> matches at the beginning of <string>:
assert search(r'\d+', '123foobar').group() == "123"
assert search(r'\d+', 'foo123bar').group() == "123"
assert match(r'\d+', '123foobar').group() == "123"
assert match(r'\d+', 'foo123bar') is None

# The MULTILINE flag does not affect re.match() in this way:
assert search('^foo', "foo\nbar\nbaz").group() == "foo"
assert search('^bar', "foo\nbar\nbaz", MULTILINE).group() == "bar"

assert match('^foo', "foo\nbar\nbaz").group() == "foo"
assert match('^bar', "foo\nbar\nbaz", MULTILINE) is None

# re.fullmatch(<regex>, <string>, flags=0)
# Looks for a regex match on an entire string.

# This is similar to re.search() and re.match(), but re.fullmatch() returns a match only
# if <regex> matches <string> in its entirety:
assert fullmatch(r'\d+', '123foo') is None
assert fullmatch(r'\d+', 'foo123') is None
assert fullmatch(r'\d+', 'foo123bar') is None
assert fullmatch(r'\d+', '123').group() == "123"
assert search(r'^\d+$', '123').group() == "123"  # The re.search() call, in which the \d+ regex is explicitly

# anchored at the start and end of the search string, is functionally equivalent.


# re.findall(<regex>, <string>, flags=0)
# Returns a list of all matches of a regex in a string.

# re.findall(<regex>, <string>) returns a list of all non-overlapping matches of <regex> in <string>. It scans
# the search string from left to right and returns all matches in the order found:
assert findall(r'\w+', '...foo,,,,bar:%$baz//|') == ['foo', 'bar', 'baz']

# If <regex> contains a capturing group, then the return list contains only contents of the group, not the entire match:
assert findall(r'#(\w+)#', '#foo#.#bar#.#baz#') == ['foo', 'bar', 'baz']

# In this case, the specified regex is #(\w+)#. The matching strings are '#foo#', '#bar#', and '#baz#'.
# But the hash (#) characters don’t appear in the return list because they’re outside the grouping parentheses.


# If <regex> contains more than one capturing group, then re.findall() returns a list of tuples containing
# the captured groups. The length of each tuple is equal to the number of groups specified:

# In this example, the regex contains two capturing groups, so re.findall() returns a list of three two-tuples,
# each containing two captured matches:
assert findall(r'(\w+),(\w+)', 'foo,bar,baz,qux,quux,corge') == [('foo', 'bar'), ('baz', 'qux'), ('quux', 'corge')]

# There are three groups, so the return value is a list of two three-tuples.
assert findall(r'(\w+),(\w+),(\w+)', 'foo,bar,baz,qux,quux,corge') == [('foo', 'bar', 'baz'), ('qux', 'quux', 'corge')]

# re.finditer(<regex>, <string>, flags=0)
# Returns an iterator that yields regex matches.

# re.finditer(<regex>, <string>) scans <string> for non-overlapping matches of <regex> and returns an iterator
# that yields the match objects from any it finds. It scans the search string from left to right and returns matches
# in the order it finds them:
it = finditer(r'\w+', '...foo,,,,bar:%$baz//|')
match_obj = next(it)
assert match_obj.group() == "foo"
assert next(it).group() == "bar"
assert next(it).group() == "baz"

# assert next(it) ->  StopIteration, because there aren't more matches in the search string


# re.findall() and re.finditer() are very similar, but they differ in two respects:
# re.findall() returns a list, whereas re.finditer() returns an iterator.
# The items in the list that re.findall() returns are the actual matching strings, whereas the items yielded
# by the iterator that re.finditer() returns are match objects.


# 2. SUBSTITUTION FUNCTIONS

# Substitution functions replace portions of a search string that match a specified regex.

# 2.1. re.sub()	scans a string for regex matches, replaces the matching portions of the string with the
# specified replacement string, and returns the result

# 2.2. re.subn() behaves just like re.sub() but also returns information regarding the number of substitutions made.

# Both re.sub() and re.subn() create a new string with the specified substitutions and return it. The original string
# remains unchanged. (Remember that strings are immutable in Python, so it wouldn’t be possible for these functions
# to modify the original string.).

# 2.1. re.sub(<regex>, <repl>, <string>, count=0, flags=0)
# Returns a new string that results from performing replacements on a search string.

# re.sub(<regex>, <repl>, <string>) finds the leftmost non-overlapping occurrences of <regex> in <string>, replaces
# each match as indicated by <repl>, and returns the result. <string> remains unchanged.

# <repl> can be either a string or a function, as explained below.

# Substitution by String
# If <repl> is a string, then re.sub() inserts it into <string> in place of any sequences that match <regex>:
s = 'foo.123.bar.789.baz'
assert sub(r'\d+', '#', s) == "foo.#.bar.#.baz"  # sub returns the modified string
assert sub('[a-z]+', '(*)', s) == "(*).123.(*).789.(*)"

# re.sub() replaces numbered backreferences (\<n>) in <repl> with the text of the corresponding captured group:
assert sub(r'(\w+),bar,baz,(\w+)', r'\2,bar,baz,\1', 'foo,bar,baz,qux') == "qux,bar,baz,foo"

# Here, captured groups 1 and 2 contain 'foo' and 'qux'. In the replacement string '\2,bar,baz,\1',
# 'foo' replaces \1 and 'qux' replaces \2.


# You can also refer to named backreferences created with (?P<name><regex>) in the replacement string
# using the metacharacter sequence \g<name>:
assert sub(r'foo,(?P<w1>\w+),(?P<w2>\w+),qux', r'foo,\g<w2>,\g<w1>,qux', 'foo,bar,baz,qux') == "foo,baz,bar,qux"

# In fact, you can also refer to numbered backreferences this way by specifying the group number inside
# the angled brackets:
assert sub(r'foo,(\w+),(\w+),qux', r'foo,\g<2>,\g<1>,qux', 'foo,bar,baz,qux') == "foo,baz,bar,qux"

# You may need to use this technique to avoid ambiguity in cases where a numbered backreference is immediately f
# ollowed by a literal digit character. For example, suppose you have a string like 'foo 123 bar' and want to
# add a '0' at the end of the digit sequence. You might try this:

# sub(r'(\d+)', r'\10', 'foo 123 bar') \10 means first group + 0 -> error: invalid group reference 10 at position 1
# Alas, the regex parser in Python interprets \10 as a backreference to the tenth captured group, which doesn’t
# exist in this case. Instead, you can use \g<1> to refer to the group:
assert sub(r'(\d+)', r'\g<1>0', 'foo 123 bar') == "foo 1230 bar"

# The backreference \g<0> refers to the text of the entire match. This is valid even when there are
# no grouping parentheses in <regex>:
assert sub(r'\d+', '/\g<0>/', 'foo 123 bar') == "foo /123/ bar"

# If <regex> specifies a zero-length match (match = '', span = (0, 0)), then re.sub() will substitute <repl>
# into every character position in the string:
assert sub('x*', '-', 'foo') == "-f-o-o-"


# If re.sub() doesn’t find any matches, then it always returns <string> unchanged.


# Substitution by Function
# If you specify <repl> as a function, then re.sub() calls that function for each match found. It passes each
# corresponding match object as an argument to the function to provide information about the match. The function
# return value then becomes the replacement string:

def f(match_obj):
    s = match_obj.group(0)  # The matching string

    # s.isdigit() returns True if all characters in s are digits
    if s.isdigit():
        return str(int(s) * 10)
    else:
        return s.upper()


assert sub(r'\w+', f, 'foo.10.bar.20.baz.30') == "FOO.100.BAR.200.BAZ.300"
# In this example, f() gets called for each match. As a result, re.sub() converts each alphanumeric portion
# of <string> to all uppercase and multiplies each numeric portion by 10.

# If you specify a positive integer for the optional count parameter, then re.sub() performs at most
# that many replacements:
assert sub(r'\w+', 'xxx', 'foo.bar.baz.qux') == "xxx.xxx.xxx.xxx"
assert sub(r'\w+', 'xxx', 'foo.bar.baz.qux', count=2) == "xxx.xxx.baz.qux"

# As with most re module functions, re.sub() accepts an optional <flags> argument as well.


# 2.2. re.subn(<regex>, <repl>, <string>, count=0, flags=0)
# Returns a new string that results from performing replacements on a search string and also returns
# the number of substitutions made.

# re.subn() is identical to re.sub(), except that re.subn() returns a two-tuple consisting of the modified string
# and the number of substitutions made:

assert subn(r'\w+', 'xxx', 'foo.bar.baz.qux') == ("xxx.xxx.xxx.xxx", 4)
assert subn(r'\w+', 'xxx', 'foo.bar.baz.qux', count=2) == ("xxx.xxx.baz.qux", 2)


def f(match_obj):
    m = match_obj.group(0)
    if m.isdigit():
        return str(int(m) * 10)
    else:
        return m.upper()


assert subn(r'\w+', f, 'foo.10.bar.20.baz.30') == ("FOO.100.BAR.200.BAZ.300", 6)
# In all other respects, re.subn() behaves just like re.sub().


# 3. UTILITY FUNCTIONS

# 3.1. re.split(<regex>, <string>, maxsplit=0, flags=0)
# Splits a string into substrings.

# re.split(<regex>, <string>) splits <string> into substrings using <regex> as the delimiter
# and returns the substrings as a list.

# The following example splits the specified string into substrings delimited by a comma (,), semicolon (;),
# or slash (/) character, surrounded by any amount of whitespace:
assert split('\s*[,;/]\s*', 'foo,bar  ;  baz / qux') == ['foo', 'bar', 'baz', 'qux']

# If <regex> contains capturing groups, then the return list includes the matching delimiter strings as well:
assert split('(\s*[,;/]\s*)', 'foo,bar  ;  baz / qux') == ['foo', ',', 'bar', '  ;  ', 'baz', ' / ', 'qux']

# This can be useful if you want to split <string> apart into delimited tokens, process the tokens in some way,
# then piece the string back together using the same delimiters that originally separated them:

string = 'foo,bar  ;  baz / qux'
regex = r'(\s*[,;/]\s*)'
a = split(regex, string)
assert a == ['foo', ',', 'bar', '  ;  ', 'baz', ' / ', 'qux']

# Enclose each token in <>'s
for i, s in enumerate(a):
    # This will be True for the tokens but not the delimiters
    if not fullmatch(regex, s):
        a[i] = f'<{s}>'

# Put the tokens back together using the same delimiters
s = ''.join(a)
assert s == "<foo>,<bar>  ;  <baz> / <qux>"

# If you need to use groups but don’t want the delimiters included in the return list, then you can
# use noncapturing groups:
string = 'foo,bar  ;  baz / qux'
regex = r'(?:\s*[,;/]\s*)'
assert split(regex, string) == ['foo', 'bar', 'baz', 'qux']

# If the optional maxsplit argument is present and greater than zero, then re.split() performs at most that many
# splits. The final element in the return list is the remainder of <string> after all the splits have occurred:
s = 'foo, bar, baz, qux, quux, corge'
assert split(r',\s*', s) == ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
assert split(r',\s*', s, maxsplit=0) == ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
assert split(r',\s*', s, maxsplit=3) == ['foo', 'bar', 'baz', 'qux, quux, corge']

# Explicitly specifying maxsplit=0 is equivalent to omitting it entirely. If maxsplit is negative, then re.split()
# returns <string> unchanged (in case you were looking for a rather elaborate way of doing nothing at all):
assert split(r',\s*', s, maxsplit=-1) == ["foo, bar, baz, qux, quux, corge"]

# If <regex> contains capturing groups (which means () ) so that the return list includes delimiters, and <regex>
# matches the start of <string>, then re.split() places an empty string as the first element in the return list.
# Similarly, the last item in the return list is an empty string if <regex> matches the end of <string>:
assert split('(/)', '/foo/bar/baz/') == ['', '/', 'foo', '/', 'bar', '/', 'baz', '/', '']

# In this case, the <regex> delimiter is a single slash (/) character. In a sense, then, there’s an empty string
# to the left of the first delimiter and to the right of the last one. So it makes sense that re.split() places
# empty strings as the first and last elements of the return list.

# 3.2. re.escape(<regex>)
# Escapes characters in a regex.
# re.escape(<regex>) returns a copy of <regex> with each nonword character (anything other than a letter, digit,
# or underscore) preceded by a backslash.

# This is useful if you’re calling one of the re module functions, and the <regex> you’re passing in has a lot
# of special characters that you want the parser to take literally instead of as metacharacters. It saves you
# the trouble of putting in all the backslash characters manually:

assert match('foo^bar(baz)|qux', 'foo^bar(baz)|qux') is None
assert match('foo\^bar\(baz\)\|qux', 'foo^bar(baz)|qux').group() == "foo^bar(baz)|qux"

assert (escape('foo^bar(baz)|qux') == 'foo\^bar\(baz\)\|qux') is True
assert match(escape('foo^bar(baz)|qux'), 'foo^bar(baz)|qux').group() == "foo^bar(baz)|qux"

# In the first example, there isn’t a match on line 1 because the regex 'foo^bar(baz)|qux' contains special characters
# that behave as metacharacters. In the second example, they’re explicitly escaped with backslashes, so a match occurs.
# The third and the fourth examples demonstrate that you can achieve the same effect using re.escape().

# Correct variant of the previous example with right metacharcters:
assert match('foobar(baz)|qux', 'foobarbaz').group() == "foobarbaz"
assert match('foobar(baz)|qux', 'qux').group() == "qux"
