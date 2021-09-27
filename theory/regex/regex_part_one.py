from re import search

# REGULAR EXPRESSIONS. PART I.
# METACHARACTERS SUPPORTED BY THE re MODULE.


# A regex is a special sequence of characters that defines a pattern for complex string-matching functionality.
# search(<regex>, <string>) scans <string> looking for the first location where the pattern <regex> matches.
# If a match is found, then search() returns a match object. Otherwise, it returns None.
if search("123", "foo123bazz"):
    print("I've found it!")
else:
    print("This pattern is absent")

# m.group(<n>) returns a string containing the <n>th captured match.
# With one argument, .group() returns a single captured match. Note that the arguments are one-based,
# not zero-based. So, m.group(1) refers to the first captured match, m.group(2) to the second, and so on:
m = search('(\w+),(\w+),(\w+)', 'foo,quux,baz')

assert m.groups() == ('foo', 'quux', 'baz')
assert m.group(1) == "foo"
assert m.group(2) == "quux"
assert m.group(3) == "baz"

# Since the numbering of captured matches is one-based, and there isn’t any group numbered zero,
# m.group(0) has a special meaning:
assert m.group(0) == "foo,quux,baz"

# m.group(<n1>, <n2>, ...) returns a tuple containing the specified captured matches
m = search('(\w+),(\w+),(\w+)', 'foo,quux,baz')

assert m.group(1, 2) == ("foo", "quux")
assert m.group(3, 2, 1) == ("baz", "quux", "foo")

# Consider again the problem of how to determine whether a string
# contains any three consecutive decimal digit characters.

# In a regex, a set of characters specified in square brackets ([]) makes up a character class. This metacharacter
# sequence matches any single character that is in the class, as demonstrated in the following example:
m = search('[0-9]', 'foo123bar')
assert m.group() == "1"

m = search('[0-9][0-9][0-9]', 'foo123bar')
assert m.group() == "123"

assert search('[0-9][0-9][0-9]', '12foo34') is None

#  .groups() returns a tuple containing all the captured groups from a regex match.
m = search('(\w+),(\w+),(\w+)', 'foo,quux,baz')
assert m.groups() == ("foo", "quux", "baz")

# [] - specifies a specific set of characters to match.
#
# Characters contained in square brackets ([]) represent a character class—an
# enumerated set of characters to match from. A character class metacharacter
# sequence will match any single character contained in the class:
m = search('ba[artz]', 'foobarqux')
assert m.group() == "bar"

m = search('ba[artz]', 'foobazqux')
assert m.group() == "baz"

# A character class can also contain a range of characters separated by a hyphen (-),
# in which case it matches any single character within the range.
# For example,
# [a-z] matches any lowercase alphabetic character between 'a' and 'z'
# [A-Z] matches any lowercase alphabetic character between 'A' and 'Z'
# [0-9] matches any digit character
# [0-9a-fA-f] matches any hexadecimal digit character
m = search('[a-z][a-z][a-z]', 'FOObar')
assert m.group() == "bar"

m = search('[0-9][0-9]', 'foo123bar')
assert m.group() == "12"

m = search('[0-9a-fA-f]', '--- a0 ---')
assert m.group() == "a"

# You can complement a character class by specifying ^ as the first character, in which case it matches any
# character that isn’t in the set. In the following example, [^0-9] matches any character that isn’t a digit:
m = search('[^0-9]', '12345foo')
assert m.group() == "f"  # because it is the first symbol, which isn't [0-9]

# If a ^ character appears in a character class but isn’t the first character,
# then it has no special meaning and matches a literal '^' character:
m = search('[#:^]', 'foo^bar:baz#qux')
assert m.group() == "^"

# As you’ve seen, you can specify a range of characters in a character class by separating
# characters with a hyphen (-). What if you want the character class to include a literal
# hyphen character? You can place it as the first or last character or escape it with
# a backslash (\):
m = search('[-abc]', '123-456')
assert m.group() == "-"
m = search('[abc-]', '123-456')
assert m.group() == "-"
m = search('[ab\-c]', '123-456')
assert m.group() == "-"

# If you want to include a literal ']' in a character class, then you can place it as
# the first character or escape it with backslash:
m = search('[]]', 'foo[1]')
assert m.group() == "]"
m = search('[ab\]cd]', 'foo[1]')
assert m.group() == "]"

# Other regex metacharacters lose their special meaning inside a character class:
m = search('[)*+|]', '123+456')
assert m.group() == "+"
m = search('[)*+|]', '123*456')
assert m.group() == "*"
# As you know, * and + have special meanings in a regex in Python. They designate
# repetition, but in this example, they’re inside a character class, so they match themselves literally.


# The . metacharacter matches any single character except a newline:
m = search('1.3', 'foo123bar')
assert m.group() == "123"

assert search('1.3', 'foo13bar') is None

m = search('foo.bar', 'fooxbar')
assert m.group() == "fooxbar"

assert search('foo.bar', 'foobar') is None

assert search('foo.bar', 'foo\nbar') is None  # because "\n" character means newline

# \w matches any alphanumeric word character. Word characters are uppercase and lowercase letters, digits,
# and the underscore (_) character, so \w is essentially shorthand for [a-zA-Z0-9_]:
# \W is the opposite. It matches any non-word character and is equivalent to [^a-zA-Z0-9_]:
m = search('\w', '#(.a$@&')
assert m.group() == "a"

m = search('[a-zA-Z0-9_]', '#(.a$@&')
assert m.group() == "a"

m = search('\W', 'a_1*3Qb')
assert m.group() == "*"
m = search('[^a-zA-Z0-9_]', 'a_1*3Qb')
assert m.group() == "*"

# \d matches any decimal digit character and is essentially equivalent to [0-9].
# \D matches any character that isn’t a decimal digit and is equivalent to [^0-9].
m = search('\d', 'abc4def')
assert m.group() == "4"
m = search('\D', '234Q678')
assert m.group() == "Q"

# \s matches any whitespace character
m = search('\s', 'foo\nbar baz')
assert m.group() == "\n"
# Note that, unlike the dot wildcard metacharacter, \s does match a newline character.

# \S matches any character that isn’t whitespace
m = search('\S', '  \n foo  \n  ')
assert m.group() == "f"
# Again, \s and \S consider a newline to be whitespace.


# The character class sequences \w, \W, \d, \D, \s, and \S can appear inside a square bracket character class as well:
assert search('[\d\w\s]', '---3---').group() == "3"
assert search('[\d\w\s]', '---a---').group() == "a"
assert search('[\d\w\s]', '--- ---').group() == " "

# In this case, [\d\w\s] matches any digit, word, or whitespace character. And since \w includes \d,
# the same character class could also be expressed slightly shorter as [\w\s].


# backslash (\) removes the special meaning of a metacharacter.
assert search('.', 'foo.bar').group() == "f"  # because dot (.) means any character
assert search('\.', 'foo.bar').group() == "."  # because "\." means "."

# If we have s = "foo\baz" and use "\\" for searh, there will be error. =>
# The Python interpreter is the first to process the string literal '\\'.
# It interprets that as an escaped backslash and passes only a single backslash to re.search().
# The regex parser receives just a single backslash, which isn’t a meaningful regex, so the messy error ensues.

# There are two ways around this. First, you can escape both backslashes in the original string literal:
assert search('\\\\', "foo\ baz").group() == "\\"

# Doing so causes the following to happen:
# The interpreter sees '\\\\' as a pair of escaped backslashes. It reduces each pair to a single backslash
# and passes '\\' to the regex parser. The regex parser then sees \\ as one escaped backslash. As a <regex>, that
# matches a single backslash character. You can see from the match object that it matched the backslash at index 3
# in s as intended. It’s cumbersome, but it works.

# The second, and probably cleaner, way to handle this is to specify the <regex> using a raw string:
assert search(r'\\', "foo\ baz").group() == "\\"

# This suppresses the escaping at the interpreter level. The string '\\' gets passed unchanged to the regex
# parser, which again sees one escaped backslash as desired.


# ^ and \A - anchors a match to the start of <string>.

# When the regex parser encounters ^ or \A, the parser’s current position must be at the beginning of the search string
# for it to find a match.
# In other words, regex ^foo stipulates that 'foo' must be present not just any old place in the search string,
# but at the beginning:
assert search('^foo', 'foobar').group() == "foo"
assert search('^foo', 'barfoo') is None

# \A functions similarly:
assert search('\Afoo', 'foobar').group() == "foo"
assert search('\Afoo', 'barfoo') is None

# ^ and \A behave slightly differently from each other in MULTILINE mode.


# $ and \Z anchors a match to the end of <string>.

# When the regex parser encounters $ or \Z, the parser’s current position must be at the end of
# the search string for it to find a match. Whatever precedes $ or \Z must constitute the end of the search string:
assert search('bar$', 'foobar').group() == "bar"
assert search('bar$', 'barfoo') is None

assert search('bar\Z', 'foobar').group() == "bar"
assert search('bar\Z', 'barfoo') is None

# As a special case, $ (but not \Z) also matches just before a single newline at the end of the search string:
assert search('bar$', 'foobar\n').group() == "bar"

# In this example, 'bar' isn’t technically at the end of the search string because it’s followed by one
# additional newline character. But the regex parser lets it slide and calls it a match anyway. This
# exception doesn’t apply to \Z.

# $ and \Z behave slightly differently from each other in MULTILINE mode.


# \b anchors a match to a word boundary.

# \b asserts that the regex parser’s current position must be at the beginning or end of a word. A word
# consists of a sequence of alphanumeric characters or underscores ([a-zA-Z0-9_]), the same as for
# the \w character class:
assert search(r'\bbar', 'foo barfoo').group() == "bar"  # because there’s a word boundary at the start of 'bar'
assert search(r'\bbar', 'foo.bar').group() == "bar"  # because there’s a word boundary at the start of 'bar'

assert search(r'\bbar', 'foobar') is None  # because the "foobar" is one word

assert search(r'foo\b', 'foo barfoo').group() == "foo"  # because a word boundary exists at the end of 'foo'
assert search(r'foo\b', 'foo.bar').group() == "foo"  # because a word boundary exists at the end of 'foo'

assert search(r'foo\b', 'foobar') is None  # because the "foobar" is one word

# Using the \b anchor on both ends of the <regex> will cause it to match when it’s present in the search
# string as a whole word:
assert search(r'\bbar\b', 'foo bar baz').group() == "bar"
assert search(r'\bbar\b', 'foo(bar)baz').group() == "bar"

assert search(r'\bbar\b', 'foobarbaz') is None

# \B does the opposite of \b. It asserts that the regex parser’s current position must not be at
# the start or end of a word
assert search(r'\Bfoo\B', 'foo') is None
assert search(r'\Bfoo\B', '.foo.') is None

assert search(r'\Bfoo\B', 'barfoobaz').group() == "foo"  # because no word boundary exists at the start or end of 'foo'

# QUANTIFIERS


# A quantifier metacharacter immediately follows a portion of a <regex> and indicates
# how many times that portion must occur for the match to succeed.


# * matches zero or more repetitions of the preceding regex.

# For example, a* matches zero or more 'a' characters. That means it would match an empty
# string, 'a', 'aa', 'aaa', and so on.
assert search('foo-*bar', 'foobar').group() == "foobar"  # Zero dashes
assert search('foo-*bar', 'foo-bar').group() == "foo-bar"  # One dash
assert search('foo-*bar', 'foo--bar').group() == "foo--bar"  # Two dashes

# .* matches zero or more occurrences of any character up to a line break.
# (Remember that the . wildcard metacharacter doesn’t match a newline.)
assert search('foo.*bar', '# foo $qux@grault % bar #').group() == "foo $qux@grault % bar"

# + matches one or more repetitions of the preceding regex.
# This is similar to *, but the quantified regex must occur at least once
assert search('foo-+bar', 'foobar') is None  # Zero dashes
assert search('foo-+bar', 'foo-bar').group() == "foo-bar"  # One dash
assert search('foo-+bar', 'foo--bar').group() == "foo--bar"  # Two dashes

# Remember from above that foo-*bar matched the string 'foobar' because the * metacharacter allows
# for zero occurrences of '-'. The + metacharacter, on the other hand, requires at least one occurrence of '-'.
# That means there isn’t a match on line 1 in this case.


# ? matches zero or one repetitions of the preceding regex.
# Again, this is similar to * and +, but in this case there’s only a match
# if the preceding regex occurs once or not at all:
assert search('foo-?bar', 'foobar').group() == "foobar"  # Zero dashes
assert search('foo-?bar', 'foo-bar').group() == "foo-bar"  # One dash
assert search('foo-?bar', 'foo--bar') is None  # Two dashes

# *? or +? or ?? are the non-greedy (or lazy) versions of the *, +, and ? quantifiers.

# When used alone, the quantifier metacharacters *, +, and ? are all greedy, meaning they produce the longest
# possible match. Consider this example:
assert search('<.*>', '%<foo> <bar> <baz>%').group() == "<foo> <bar> <baz>"

# Since the * metacharacter is greedy, it dictates the longest possible match, which includes everything up
# to and including the '>' character that follows 'baz'. You can see from the match object that this is
# the match produced. If you want the shortest possible match instead, then use the non-greedy
# metacharacter sequence *?

# If you want the shortest possible match instead, then use the non-greedy metacharacter sequence *?
# In this case, the match ends with the '>' character following 'foo'
assert search('<.*?>', '%<foo> <bar> <baz>%').group() == "<foo>"

# There are lazy versions of the + and ? quantifiers as well:
assert search('<.+>', '%<foo> <bar> <baz>%').group() == "<foo> <bar> <baz>"
assert search('<.+?>', '%<foo> <bar> <baz>%').group() == "<foo>"

assert search('ba?', 'baaaa').group() == "ba"  # there is zero or one "a" (greedy) after "b"
assert search('ba??', 'baaaa').group() == "b"  # there is zero "a" (non-greedy) after "b"

# {m} matches exactly m repetitions of the preceding regex.

# This is similar to * or +, but it specifies exactly how many times the preceding regex must occur
# for a match to succeed:

assert search('x-{3}x', 'x--x') is None  # Two dashes
assert search('x-{3}x', 'x---x').group() == "x---x"  # Three dashes
assert search('x-{3}x', 'x----x') is None  # Four dashes -> None

# Here, x-{3}x matches 'x', followed by exactly three instances of the '-' character, followed by another 'x'.
# The match fails when there are fewer or more than three dashes between the 'x' characters.


# {m,n} matches any number of repetitions of the preceding regex from m to n, inclusive.

# In the following example, the quantified <regex> is -{2,4}. The match succeeds when there are two, three,
# or four dashes between the 'x' characters but fails otherwise:
assert search('x-{2,4}x', 'x-x') is None
assert search('x-{2,4}x', 'x--x').group() == "x--x"
assert search('x-{2,4}x', 'x---x').group() == "x---x"
assert search('x-{2,4}x', 'x----x').group() == "x----x"
assert search('x-{2,4}x', 'x-----x') is None

# Omitting m implies a lower bound of 0, and omitting n implies an unlimited upper bound
# {,n} == {0,n}
# {m,} == m repetition or more than m
# {,} == {0,} or * which means any number of repetitions

# If you omit all of m, n, and the comma, then the curly braces no longer function as metacharacters.
# {} matches just the literal string '{}':
assert search('x{}y', 'x{}y').group() == "x{}y"

# n fact, to have any special meaning, a sequence with curly braces must fit one of the following
# patterns in which m and n are nonnegative integers, otherwise, it matches literally
assert search('x{foo}y', 'x{foo}y').group() == "x{foo}y"
assert search('x{a:b}y', 'x{a:b}y').group() == "x{a:b}y"
assert search('x{1,3,5}y', 'x{1,3,5}y').group() == "x{1,3,5}y"
assert search('x{foo,bar}y', 'x{foo,bar}y').group() == "x{foo,bar}y"

# {m,n}? is the non-greedy (lazy) version of {m,n}.
# {m,n} will match as many characters as possible, and {m,n}? will match as few as possible:
assert search('a{3,5}?', 'aaaaaaaa').group() == "aaa"

# (<regex>) defines a subexpression or group.
# This is the most basic grouping construct. A regex in parentheses just matches the contents of the parentheses
assert search('(bar)', 'foo bar baz').group() == "bar"
assert search('bar', 'foo bar baz').group() == "bar"

# As a regex, (bar) matches the string 'bar', the same as the regex bar would without the parentheses.


# A quantifier metacharacter that follows a group operates on the entire subexpression
# specified in the group as a single unit.
assert search('(bar)+', 'foo bar baz').group() == "bar"
assert search('(bar)+', 'foo barbar baz').group() == "barbar"
assert search('(bar)+', 'foo barbarbarbar baz').group() == "barbarbarbar"

# bar+	=>  the + metacharacter applies only to the character 'r'  =>  'ba' followed by one or more
# occurrences of 'r', e.g.:'bar', 'barr', 'barrr'
# (bar)+  =>  the + metacharacter applies to the entire string 'bar'  =>  one or more occurrences of 'bar'	=>
# e.g.: 'bar', 'barbar', 'barbarbar'
assert search('(ba[rz]){2,4}(qux)?', 'bazbarbazqux').group() == "bazbarbazqux"
assert search('(ba[rz]){2,4}(qux)?', 'barbar').group() == "barbar"

# \<n> matches the contents of a previously captured group.

# Within a regex in Python, the sequence \<n>, where <n> is an integer from 1 to 99, matches the contents
# of the <n>th captured group.

# Here’s a regex that matches a word, followed by a comma, followed by the same word again:
regex = r'(\w+),\1'

m = search(regex, 'foo,foo')
assert m.group() == "foo,foo"
assert m.group(1) == "foo"
# In this example, (\w+) matches the first instance of the string 'foo' and saves it as the first captured group.
# The comma matches literally. Then \1 is a backreference to the first captured group and matches 'foo' again.

assert search(regex, 'foo,qux') is None

# This example doesn’t have a match because what comes before the comma isn’t the same as what comes after it,
# so the \1 backreference doesn’t match.

# Any time you use a regex in Python with a numbered backreference, it’s a good idea to specify it as a raw string.
# Otherwise, the interpreter may confuse the backreference with an octal value.


# (?P<name><regex>) creates a named captured group.
# It is similar to grouping parantheses, but you reference the matched group by its given symbolic <name>
# instead of by its number.
m = search('(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)', 'foo,quux,baz')
assert m.group() == "foo,quux,baz"
assert m.group("w1") == "foo"
assert m.group("w2") == "quux"
assert m.group("w3") == "baz"

# (?P=<name>) matches the contents of a previously captured named group.

# The (?P=<name>) metacharacter sequence is a backreference, similar to \<n>, except that it refers to a named group
# rather than a numbered group.
m = search(r'(?P<word>\w+),(?P=word)', 'foo,foo')
assert m.group("word") == "foo"

# (?P=<word>\w+) matches 'foo' and saves it as a captured group named word. Again, the comma matches literally.
# Then (?P=word) is a backreference to the named capture and matches 'foo' again.
# !!!  The angle brackets (< and >) are required around name when creating a named group but not when referring
# to it later, either by backreference or by .group()

# One more example
kate = search(r'(?P<name>\w+), (I\'m) (?P=name), (my name is) (?P=name)', 'Kate, I\'m Kate, my name is Kate')
assert kate.group() == "Kate, I'm Kate, my name is Kate"
assert kate.group('name') == "Kate"

# (?:<regex>) creates a non-capturing group.

# (?:<regex>) is just like (<regex>) in that it matches the specified <regex>. But (?:<regex>) doesn’t capture t
# he match for later retrieval
m = search('(\w+),(?:\w+),(\w+)', 'foo,quux,baz')
assert m.groups() == ("foo", "baz")
assert m.group(1) == "foo"
assert m.group(2) == "baz"

#    (?(<n>)<yes-regex>|<no-regex>)  or
# (?(<name>)<yes-regex>|<no-regex>) specifies a conditional match.

regex = r'^(###)?foo(?(1)bar|baz)'
# ^(###)? indicates that the search string optionally begins with '###'.
# If it does, then the grouping parentheses around ### will create a group numbered 1.
# Otherwise, no such group will exist.
# The next portion, foo, literally matches the string 'foo'.
# Lastly, (?(1)bar|baz) matches against 'bar' if group 1 exists and 'baz' if it doesn’t.

assert search(regex, '###foobar').group() == "###foobar"  # The search string '###foobar' does start with '###',
# so the parser creates a group numbered 1. The conditional match is then against 'bar', which matches.

assert search(regex, '###foobaz') is None  # The search string '###foobaz' does start with '###', so the parser
# creates a group numbered 1. The conditional match is then against 'bar', which doesn’t match.

assert search(regex, 'foobar') is None  # The search string 'foobar' doesn’t start with '###', so there
# isn’t a group numbered 1. The conditional match is then against 'baz', which doesn’t match.

assert search(regex, 'foobaz').group() == "foobaz"  # The search string 'foobaz' doesn’t start with '###', so
# there isn’t a group numbered 1. The conditional match is then against 'baz', which matches.

# One more example

regex = r'^(?P<ch>\W)?foo(?(ch)(?P=ch)|)$'

# ^	                The start of the string
# (?P<ch>\W)	    A single non-word character, captured in a group named ch
# (?P<ch>\W)?	    Zero or one occurrences of the above
# foo	            The literal string 'foo'
# (?(ch)(?P=ch)|)	The contents of the group named ch if it exists, or the empty string if it doesn’t
# $	                The end of the string

assert search(regex, 'foo').group() == "foo"
assert search(regex, '#foo#').group() == "#foo#"
assert search(regex, '@foo@').group() == "@foo@"
assert search(regex, '#foo') is None
assert search(regex, 'foo@') is None
assert search(regex, '#foo@') is None
assert search(regex, '@foo#') is None

# (?=<lookahead_regex>) creates a positive lookahead assertion.
# It asserts that what follows the regex parser’s current position must match <lookahead_regex>:
assert search('foo(?=[a-z])', 'foobar').group() == "foo"
# The lookahead assertion (?=[a-z]) specifies that what follows 'foo' must be a lowercase alphabetic character.
# In this case, it’s the character 'b', so a match is found.

assert search('foo(?=[a-z])', 'foo123') is None
# The next character after 'foo' is '1', so there isn’t a match and lookahead fails

# What’s unique about a lookahead is that the portion of the search string that matches <lookahead_regex> isn’t
# consumed, and it isn’t part of the returned match object.
# Compare:
assert search('foo(?=[a-z])', 'foobar').group() == "foo"
assert search('foo([a-z])', 'foobar').group() == "foob"

# Here’s another example illustrating how a lookahead differs from a conventional regex in Python:
m = search('foo(?=[a-z])(?P<ch>.)', 'foobar')
assert m.group('ch') == "b"  # parser doesn't advance the 'b', so it is the last char, which is captured by "ch"
m = search('foo([a-z])(?P<ch>.)', 'foobar')
assert m.group('ch') == 'a'

# (?!<lookahead_regex>) creates a negative lookahead assertion.
# It asserts that what follows the regex parser’s current position must not match <lookahead_regex>.
assert search('foo(?![a-z])', 'foobar') is None  # because that what follows 'foo' should not be
# lowercase alphabetic character
assert search('foo(?![a-z])', 'foo123').group() == "foo"  # because 'that what follows 'foo' can ne numbers

# (?<=<lookbehind_regex>) creates a positive lookbehind assertion.
# It asserts that what precedes the regex parser’s current position must match <lookbehind_regex>
assert search('(?<=foo)bar', 'foobar').group() == "bar"
assert search('(?<=qux)bar', 'foobar') is None

# There’s a restriction on lookbehind assertions that doesn’t apply to lookahead assertions.
# The <lookbehind_regex> in a lookbehind assertion must specify a match of fixed length.

# For example, the following isn’t allowed because the length of the string matched by a+ is indeterminate:

# search('(?<=a+)def', 'aaadef') -> there is an error
# but the next is OK

assert search('(?<=a{3})def', "aaadef").group() == "def"  # because a{3} has a fixed length of three,
# so a{3} is valid in a lookbehind assertion.

# (?<! <lookbehind_regex>) creates a negative lookbehind assertion.
# It asserts that what precedes the regex parser’s current position must not match <lookbehind_regex>:
assert search('(?<!foo)bar', "foobar") is None  # because there shouldn't be "foo" before "bar"
assert search('(?<!foo)bar', "quxbar").group() == "bar"  # because "qux" isn't "foo"
# As with the positive lookbehind assertion, <lookbehind_regex> must specify a match of fixed length.


# MISCELLANEOUS METAHARACTERS

# (?#...) specifies a comment.

# The regex parser ignores anything contained in the sequence (?#...):
assert search('bar(?#This is a comment for long regex) *baz', 'foo bar baz qux').group() == 'bar baz'

# Vertical bar, or pipe (|) specifies a set of alternatives on which to match.
# An expression of the form <regex1>|<regex2>|...|<regexn> matches at most one of the specified <regexi> expressions:
assert search('foo|bar|baz', 'bar').group() == "bar"
assert search('foo|bar|baz', 'baz').group() == "baz"
assert search('foo|bar|baz', 'quux') is None

# Alternation is non-greedy. The regex parser looks at the expressions separated by | in left-to-right order and
# returns the first match that it finds. The remaining expressions aren’t tested, even if one of them would
# produce a longer match:
assert search('foo', 'foograult').group() == "foo"
assert search('grault', 'foograult').group() == "grault"
assert search('foo|grault', 'foograult').group() == "foo"

# It's possible to combine character in order to achieve whatever level of complexity you need.
# For example:
assert search('(foo|bar|baz)+', 'foofoofoo').group() == "foofoofoo"
assert search('(foo|bar|baz)+', 'bazbazbazbaz').group() == "bazbazbazbaz"
assert search('(foo|bar|baz)+', 'barbazfoo').group() == 'barbazfoo'
assert search('([0-9]+|[a-f]+)', '456').group() == "456"
assert search('([0-9]+|[a-f]+)', 'ffda').group() == "ffda"


print("All is OK!")
