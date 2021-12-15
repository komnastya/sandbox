# s.center(<width>[, <fill>]) centers a string in a field:
assert 'foo'.center(10) == '   foo    '
assert 'foo'.center(10, '-') == '---foo----'
assert 'foo'.center(2) == 'foo'

# s.expandtabs(tabsize=8) expands tabs in a string:
assert 'a\tb\tc'.expandtabs() == 'a       b       c'
assert 'aaa\tbbb\tc'.expandtabs() == 'aaa     bbb     c'

# tabsize is an optional keyword parameter specifying alternate tab stop columns:
assert 'a\tb\tc'.expandtabs(4) == 'a   b   c'
assert 'aaa\tbbb\tc'.expandtabs(tabsize=5) == 'aaa  bbb  c'

# s.ljust(<width>[, <fill>]) left-justifies a string in field:
assert 'foo'.ljust(10) == 'foo       '
assert 'foo'.ljust(10, '-') == 'foo-------'
assert 'foo'.ljust(2) == 'foo'

# s.lstrip([<chars>]) trims leading characters from a string:
assert '   foo bar baz   '.lstrip() == 'foo bar baz   '
assert '\t\nfoo\t\nbar\t\nbaz'.lstrip() == 'foo\t\nbar\t\nbaz'
assert 'http://www.realpython.com'.lstrip('/:pth') == 'www.realpython.com'

# s.replace(<old>, <new>[, <count>]) replaces occurrences of a substring within a string:
assert 'foo bar foo baz foo qux'.replace('foo', 'grault') == 'grault bar grault baz grault qux'
assert 'foo bar foo baz foo qux'.replace('foo', 'grault', 2) == 'grault bar grault baz foo qux'

# s.rjust(<width>[, <fill>]) right-justifies a string in a field:
assert 'foo'.rjust(10) == '       foo'
assert 'foo'.rjust(10, '-') == '-------foo'
assert 'foo' == 'foo'

# s.rstrip([<chars>]) trims trailing characters from a string:
assert '   foo bar baz   '.rstrip() == '   foo bar baz'
assert 'foo\t\nbar\t\nbaz\t\n'.rstrip() == 'foo\t\nbar\t\nbaz'
assert 'foo.$$$;'.rstrip(';$.') == 'foo'

# s.strip([<chars>]) strips characters from the left and right ends of a string:
assert '   foo bar baz\t\t\t'.strip() == 'foo bar baz'
assert 'www.realpython.com'.strip('w.moc') == 'realpython'

assert '   foo bar baz\t\t\t'.lstrip().rstrip() == '   foo bar baz\t\t\t'.strip()

# s.zfill(<width>) pads a string on the left with zeros:
assert '42'.zfill(5) == '00042'

# If s contains a leading sign, it remains at the left edge of the result string after zeros are inserted:
assert '+42'.zfill(8) == '+0000042'
assert '-42'.zfill(8) == '-0000042'
assert '+42'.zfill(2) == '+42'
assert 'foo'.zfill(6) == '000foo'

# s.partition(<sep>) divides a string based on a separator.
# s.partition(<sep>) splits s at the first occurrence of string <sep>:
assert 'foo.bar'.partition('.') == ('foo', '.', 'bar')
assert 'foo@@bar@@baz'.partition('@@') == ('foo', '@@', 'bar@@baz')
assert 'foo.bar'.partition('@@') == ('foo.bar', '', '')

# s.rpartition(<sep>) divides a string based on a separator.
# s.rpartition(<sep>) functions exactly like s.partition(<sep>), except that s is split at the last occurrence of
# <sep> instead of the first occurrence:
assert 'foo@@bar@@baz'.partition('@@') == ('foo', '@@', 'bar@@baz')
assert 'foo@@bar@@baz'.rpartition('@@') == ('foo@@bar', '@@', 'baz')

# s.rsplit(sep=None, maxsplit=-1) splits a string into a list of substrings:
assert 'foo bar baz qux'.rsplit() == ['foo', 'bar', 'baz', 'qux']
assert 'foo\n\tbar   baz\r\fqux'.rsplit() == ['foo', 'bar', 'baz', 'qux']
assert 'foo.bar.baz.qux'.rsplit(sep='.') == ['foo', 'bar', 'baz', 'qux']
assert 'foo...bar'.rsplit(sep='.') == ['foo', '', '', 'bar']
assert 'foo\t\t\tbar'.rsplit() == ['foo', 'bar']

# If the optional keyword parameter <maxsplit> is specified, a maximum of that many splits are performed, starting
# from the right end of s:
assert 'www.realpython.com'.rsplit(sep='.', maxsplit=1) == ['www.realpython', 'com']
assert 'www.realpython.com'.rsplit(sep='.', maxsplit=-1) == ['www', 'realpython', 'com']
assert 'www.realpython.com'.rsplit(sep='.') == ['www', 'realpython', 'com']

medicine1 = ['Morning', 'Dispirine', '1 mg']
medicine2 = ['Noon', 'Arinic', '2 mg']
medicine3 = ['Evening', 'Long_capsule_name', '32 mg']

for medicine in [medicine1, medicine2, medicine3]:
    for entry in medicine:
        print(entry.ljust(25), end='')
    print()

# s.split(sep=None, maxsplit=-1) splits a string into a list of substrings.
# s.split() behaves exactly like s.rsplit(), except that if <maxsplit> is specified, splits are counted from the left
# end of s rather than the right end:
assert 'www.realpython.com'.split(sep='.', maxsplit=1) == ['www', 'realpython.com']
assert 'www.realpython.com'.split(sep='.', maxsplit=-1) == ['www', 'realpython', 'com']
assert 'www.realpython.com'.split(sep='.') == ['www', 'realpython', 'com']

assert 'www.realpython.com'.split(sep='.') == 'www.realpython.com'.rsplit(sep='.')

# s.splitlines([<keepends>]) breaks a string at line boundaries:
assert 'foo\nbar\r\nbaz\fqux\u2028quux'.splitlines() == ['foo', 'bar', 'baz', 'qux', 'quux']

# If consecutive line boundary characters are present in the string, they are assumed to delimit blank lines, which will
# appear in the result list:
assert 'foo\f\f\fbar'.splitlines() == ['foo', '', '', 'bar']

# If the optional <keepends> argument is specified and is truthy, then the lines boundaries are retained in the result
# strings:
assert 'foo\nbar\nbaz\nqux'.splitlines(True) == ['foo\n', 'bar\n', 'baz\n', 'qux']
assert 'foo\nbar\nbaz\nqux'.splitlines(1) == ['foo\n', 'bar\n', 'baz\n', 'qux']
