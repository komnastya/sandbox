# https://realpython.com/python-formatted-output/#the-string-format-method-nested-replacement-fields
# The String .format() Method: Nested Replacement Fields

# Inside a replacement field, you can specify a nested set of curly braces ({}) that contains a name or number referring
# to one of the method’s positional or keyword arguments.

w = 10
p = 2
assert '{2:{0}.{1}f}'.format(w, p, 123.456) == '    123.46'
assert '{val:{wid}.{pr}f}'.format(wid=w, pr=p, val=123.456) == '    123.46'
assert '{0:10.2f}'.format(123.456) == '    123.46'

# Here (line 9), the <name> component of the replacement field is 2, which indicates the third positional parameter whose value
# is 123.456. This is the value to be formatted. The nested replacement fields {0} and {1} correspond to the first and
# second positional parameters, w and p. These occupy the <width> and <prec> locations in <format_spec> and allow field
# width and precision to be evaluated at run-time.

# You can specify any portion of <format_spec> using nested replacement fields.
# In the following example, the presentation type <type> is specified by a nested replacement field and determined
# dynamically:
assert [bin(10), oct(10), hex(10)] == ['0b1010', '0o12', '0xa']

s = []
for t in ('b', 'o', 'x'):
    s.append('{0:#{type}}'.format(10, type=t))
assert s == ['0b1010', '0o12', '0xa']

# Here, the grouping character <group> is nested:
assert '{0:{grp}d}'.format(123456789, grp='_') == '123_456_789'
assert '{0:{grp}d}'.format(123456789, grp=',') == '123,456,789'

# Nesting also works with f-strings:

a = ['foo', 'bar', 'baz', 'qux', 'quux']
w = 4
assert f'{len(a):0{w}d}' == '0005'

n = 123456789
sep = '_'
assert f'{(n * n):{sep}d}' == '15_241_578_750_190_521'
