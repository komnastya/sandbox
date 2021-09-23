from re import ASCII, DEBUG, DOTALL, I, IGNORECASE, M, MULTILINE, S, UNICODE, VERBOSE, X, search

# REGULAR EXPRESSION. PART II.
# MODIFIED REGULAR EXPRESSION MATCHING WITH FLAGS.


# Most of the functions in the re module take an optional <flags> argument. This includes the function
# you’re now very familiar with, re.search().

# re.search(<regex>, <string>, <flags>) scans a string for a regex match, applying the specified modifier <flags>.
# Flags modify regex parsing behavior, allowing you to refine your pattern matching even further.


# re.I
# re.IGNORECASE
# Makes matching case insensitive.
assert search('a+', 'aaaAAA').group() == "aaa"
assert search('A+', 'aaaAAA').group() == "AAA"

assert search('a+', 'aaaAAA', I).group() == "aaaAAA"
assert search('A+', 'aaaAAA', IGNORECASE).group() == "aaaAAA"
assert search('[a-z]+', 'aBcDeF').group() == "a"
assert search('[a-z]+', 'aBcDeF', I).group() == "aBcDeF"
assert search('[a-z]+', 'aBcDeF', IGNORECASE).group() == "aBcDeF"

# re.M
# re.MULTILINE
# Causes start-of-string and end-of-string anchors to match at embedded newlines.

# By default, the ^ (start-of-string) and $ (end-of-string) anchors match only at the beginning and
# end of the search string:
s = 'foo\nbar\nbaz'

assert search('^foo', s).group() == "foo"
assert search('^bar', s) is None
assert search('^baz', s) is None
assert search('foo$', s) is None
assert search('bar$', s) is None
assert search('baz$', s).group() == "baz"

# If a string has embedded newlines, however, you can think of it as consisting of multiple internal lines.
# In that case, if the MULTILINE flag is set, the ^ and $ anchor metacharacters match internal lines as well:

# ^ matches at the beginning of the string or at the beginning of any line within the string
# (that is, immediately following a newline).
# $ matches at the end of the string or at the end of any line within the string (immediately preceding a newline).

# The following are the same searches as shown above:
assert search('^foo', 'foo\nbar\nbaz', MULTILINE).group() == "foo"
assert search('^bar', 'foo\nbar\nbaz', MULTILINE).group() == "bar"
assert search('^baz', 'foo\nbar\nbaz', MULTILINE).group() == "baz"

assert search('foo$', 'foo\nbar\nbaz', M).group() == "foo"
assert search('bar$', 'foo\nbar\nbaz', M).group() == "bar"
assert search('baz$', 'foo\nbar\nbaz', M).group() == "baz"

# Note: The MULTILINE flag only modifies the ^ and $ anchors in this way.
# It doesn’t have any effect on the \A and \Z anchors:
assert search('^bar', 'foo\nbar\nbaz', MULTILINE).group() == "bar"
assert search('bar$', 'foo\nbar\nbaz', MULTILINE).group() == "bar"
assert search('\Abar', 'foo\nbar\nbaz', MULTILINE) is None
assert search('bar\Z', s, MULTILINE) is None

# re.DOTALL
# re.S - shortcat
# Causes the dot (.) metacharacter to match a newline.

# Remember that by default, the dot metacharacter matches any character except the newline character.
# The DOTALL flag lifts this restriction:
assert search('foo.bar', 'foo\nbar') is None  # dot(.) doesn't include neline
assert search('foo.bar', 'foo\nbar', DOTALL).group() == "foo\nbar"  # dot(.) includes newline
assert search('foo.bar', 'foo\nbar', S).group() == "foo\nbar"

# re.VERBOSE
# re.X - shortcut
# Allows inclusion of whitespace and comments within a regex.

# The VERBOSE flag specifies a few special behaviors:
# The regex parser ignores all whitespace unless it’s within a character class or escaped with a backslash.
# If the regex contains a # character that isn’t contained within a character class or escaped with a backslash,
# then the parser ignores it and all characters to the right of it.

# Here’s an example showing how you might put this to use. Suppose you want to parse phone numbers
# that have the following format:

# Optional three-digit area code, in parentheses
# Optional whitespace
# Three-digit prefix
# Separator (either '-' or '.')
# Four-digit line number
# The following regex does the trick:

regex = r'^(\(\d{3}\))?\s*\d{3}[-.]\d{4}$'

assert search(regex, '414.9229').group() == "414.9229"
assert search(regex, '414-9229').group() == "414-9229"
assert search(regex, '(712)414-9229').group() == "(712)414-9229"
assert search(regex, '(712) 414-9229').group() == "(712) 414-9229"

# But r'^(\(\d{3}\))?\s*\d{3}[-.]\d{4}$' is an eyeful, isn’t it? Using the VERBOSE flag, you can write
# the same regex in Python like this instead:
regex = r'''^               # Start of string
            (\(\d{3}\))?    # Optional area code
            \s*             # Optional whitespace
            \d{3}           # Three-digit prefix
            [-.]            # Separator character
            \d{4}           # Four-digit line number
            $               # Anchor at end of string
              '''
assert search(regex, '414.9229', VERBOSE).group() == "414.9229"
assert search(regex, '414-9229', VERBOSE).group() == "414-9229"
assert search(regex, '(712)414-9229', X).group() == "(712)414-9229"
assert search(regex, '(712) 414-9229', X).group() == "(712) 414-9229"

# Note that triple quoting makes it particularly convenient to include embedded newlines,
# which qualify as ignored whitespace in VERBOSE mode.

# When using the VERBOSE flag, be mindful of whitespace that you do intend to be significant. Consider these examples:

assert search('foo bar', 'foo bar').group() == "foo bar"

assert search('foo bar', 'foo bar', VERBOSE) is None  # it doesn’t because the VERBOSE flag causes
# the parser to ignore the space character.

# To make this match as expected, escape the space character with a backslash or include it in a character class
assert search('foo\ bar', 'foo bar', VERBOSE).group() == "foo bar"
assert search('foo[ ]bar', 'foo bar', VERBOSE).group() == "foo bar"

# re.DEBUG
# Displays debugging information.
# The DEBUG flag causes the regex parser in Python to display debugging information
# about the parsing process to the console:
assert search('foo.bar', 'fooxbar', DEBUG).group() == "fooxbar"
# LITERAL 102
# LITERAL 111
# LITERAL 111
# ANY None
# LITERAL 98
# LITERAL 97
# LITERAL 114


# re.A
# re.ASCII
# re.U
# re.UNICODE
# re.L
# re.LOCALE
# Specify the character encoding used for parsing of special regex character classes.

# Using the default Unicode encoding, the regex parser should be able to handle any language you throw at it.

# You learned earlier that \d specifies a single digit character. The description of the \d metacharacter sequence
# states that it’s equivalent to the character class [0-9]. That happens to be true for English and Western European
# languages, but for most of the world’s languages, the characters '0' through '9' don’t represent all
# or even any of the digits.

# For example, here’s a string that consists of three Devanagari digit characters:
s = '\u0967\u096a\u096c'
# In the following example, it correctly recognizes each of the characters in the string '१४६' as a digit:
assert search('\d+', s).group() == "१४६"

# Here’s another example that illustrates how character encoding can affect a regex match in Python.
# Consider this string:
s = 'sch\u00f6n'  # 'schön'

# You should reasonably expect the regex parser to consider all of the characters in 'schön' to be word characters.
# But take a look at what happens if you search s for word characters using the \w character class
# and force an ASCII encoding.
# When you restrict the encoding to ASCII, the regex parser recognizes only the first three characters as word
# characters. The match stops at 'ö', because ASCII doesn't have this character
assert search('\w+', s, ASCII).group() == "sch"

# On the other hand, if you specify re.UNICODE or allow the encoding to default to Unicode,
# then all the characters in 'schön' qualify as word characters:
assert search('\w+', s, UNICODE).group() == "schön"
assert search('\w+', s).group() == "schön"

# The ASCII and LOCALE flags are available in case you need them for special circumstances. But in general,
# the best strategy is to use the default Unicode encoding. This should handle any world language correctly.


# COMBINING <flags> Arguments in a Function Call

# Flag values are defined so that you can combine them using the bitwise OR (|) operator.
# This allows you to specify several flags in a single function call:
# This search() call uses bitwise OR to specify both the IGNORECASE and MULTILINE flags at once.

assert search('^bar', 'FOO\nBAR\nBAZ', I | M).group() == "BAR"

# In addition to being able to pass a <flags> argument to most re module function calls, you can also modify flag
# values within a regex in Python. There are two regex metacharacter sequences that provide this capability.

# (?<flags>) sets flag value(s) for the duration of a regex.

# Within a regex, the metacharacter sequence (?<flags>) sets the specified flags for the entire expression.
# The value of <flags> is one or more letters from the set a, i, L, m, s, u, and x.

# The (?<flags>) metacharacter sequence as a whole matches the empty string.
# It always matches successfully and doesn’t consume any of the search string.
#
# The following examples are equivalent ways of setting the IGNORECASE and MULTILINE flags:
assert search('^bar', 'FOO\nBAR\nBAZ\n', I | M).group() == "BAR"
assert search('(?im)^bar', 'FOO\nBAR\nBAZ\n').group() == "BAR"

# Note that a (?<flags>) metacharacter sequence sets the given flag(s) for the entire regex no matter
# where you place it in the expression:
# In the examples below, both dot metacharacters match newlines because the DOTALL flag is in effect.
# This is true even when (?s) appears in the middle or at the end of the expression.
# But of Python 3.7, it’s deprecated to specify (?<flags>) anywhere in a regex other than at the beginning.
# It still produces the appropriate match, but you’ll get a warning message:
assert search('foo.bar(?s).baz', 'foo\nbar\nbaz').group() == "foo\nbar\nbaz"
assert search('foo.bar.baz(?s)', 'foo\nbar\nbaz').group() == "foo\nbar\nbaz"
# Compare:
assert search('(?s)foo.bar.baz', 'foo\nbar\nbaz').group() == "foo\nbar\nbaz"

# (?<set_flags>-<remove_flags>:<regex>) sets or removes flag value(s) for the duration of a group.
# It defines a non-capturing group that matches against <regex>. For the <regex> contained in the group,
# the regex parser sets any flags specified in <set_flags> and clears any flags specified in <remove_flags>.

# Values for <set_flags> and <remove_flags> are most commonly i, m, s or x.

# In the following example, the IGNORECASE flag is set for the specified group:
assert search('(?i:foo)bar', 'FOObar').group() == "FOObar"  # This produces a match because (?i:foo) dictates that
# the match against 'FOO' is case insensitive

assert search('(?i:foo)bar', 'FOOBAR') is None  # As in the previous example, the match against 'FOO' would succeed
# because it’s case insensitive. But once outside the group, IGNORECASE is no longer in effect, so the match
# against 'BAR' is case sensitive and fails.

# Here’s an example that demonstrates turning a flag off for a group:
assert search('(?-i:foo)bar', 'FOOBAR', IGNORECASE) is None
# Again, there’s no match. Although re.IGNORECASE enables case - insensitive matching for the entire call,
# the metacharacter sequence (?-i:foo) turns off IGNORECASE for the duration of that group,
# so the match against 'FOO' fails.

# As of Python 3.7, you can specify u, a, or L as <set_flags> to override the default encoding for the specified group:
s = 'sch\u00f6n'  # 'schön'
assert search('(?a:\w+)', s).group() == "sch"  # enable ASCII encoding for the whole string
assert search('(?u:\w+)', s).group() == "schön"  # enable Unicode encoding for the whole string

# You can only set encoding this way, though. You can’t remove it:
# >>> search('(?-a:\w+)', s) leads to the re.error: bad inline flags: cannot turn off flags 'a', 'u' and 'L' at

# u, a, and L are mutually exclusive. Only one of them may appear per group.

print("All is OK!")
