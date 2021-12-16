# The String .format() Method: Simple Replacement Fields

# f-strings and Python’s .format() method are, more or less, two different ways of doing the same thing, with f-strings
# being a more concise shorthand. The following expressions are essentially the same:

# f'{<expr>!<conversion>:<format_spec>}'
# '{0!<conversion>:<format_spec>}'.format(<expr>)

# A replacement field consists of three components: {[<name>][!<conversion>][:<format_spec>]}
# Each component is optional and may be omitted.

# <name> indicates which argument from the argument list is inserted into the Python format string in the given
# location.
name = 'Nastassia'
assert 'Hello, {}!'.format(name) == 'Hello, Nastassia!'

# The <conversion> component is the middle portion of a replacement field. Python can format an object as a string
# using three different built-in functions:
# str() is used by default
# repr()
# ascii()

assert '{0!s}'.format(42) == '42'
assert '{0!r}'.format(42) == '42'
assert '{0!a}'.format(42) == '42'

# Expressions in f-strings can be modified by a <conversion> or <format_spec>, just like replacement fields used in
# the .format() template. The syntax is identical. In fact, in both cases Python will format the replacement field using
# the same internal function.
assert f'Hello, {name}!' == 'Hello, Nastassia!'

assert f'{42!s}' == '42'
assert f'{42!r}' == '42'
assert f'{42!a}' == '42'

# <format_spec> represents the guts of the Python .format() method’s functionality. It contains information that exerts
# fine control over how values are formatted prior to being inserted into the template string. The general form is this:

# :[[<fill>]<align>][<sign>][#] [0] [<width>][<group>][.<prec>][<type>]
#   space       <       +    b  0     any        _             d / f / s
#   (by         >       -    o      positive     ,             x / s / g
#  default)     ^      =+    x       number                      % / b
#               =      =-                                        e / o

# :	separates the <format_spec> from the rest of the replacement field

# The <type> subcomponent specifies the presentation type, which is the type of conversion that’s performed on the
# corresponding value to produce the output.

# Possible values are:

# d	Decimal integer
assert '%d' % 42 == '42'
assert '{:d}'.format(42) == '42'
assert f'{42:d}' == '42'

# f or F	Floating point
assert '%f' % 2.1 == '2.100000'
assert '{:f}'.format(2.1) == '2.100000'
assert f'{2.1:f}' == '2.100000'

# s	String
assert '%s' % 'foobar' == 'foobar'
assert '{:s}'.format('foobar') == 'foobar'
assert f'{"foobar":s}' == 'foobar'

# x or X	Hexadecimal integer
assert '%x' % 31 == '1f'
assert '{:x}'.format(31) == '1f'
assert f'{31:x}' == '1f'

# c	Single character
assert '%c' % 35 == '#'
assert '%c' % '#' == '#'

#  .format() method requires that the value corresponding to the c presentation type be an integer:
assert '{:c}'.format(35) == '#'
# >>> '{:c}'.format('#') -> ValueError: Unknown format code 'c' for object of type 'str'

assert f'{35:c}' == '#'

# g or G	Floating point or Exponential ( depending on the magnitude of the exponent and the value specified for
# <prec>:)
assert '{:g}'.format(3.14159) == '3.14159'
assert '{:g}'.format(-123456789.8765) == '-1.23457e+08'
assert '{:G}'.format(-123456789.8765) == '-1.23457E+08'

assert f'{3.14159:g}' == '3.14159'
assert f'{-123456789.8765:g}' == '-1.23457e+08'
assert f'{-123456789.8765:G}' == '-1.23457E+08'

x = 1e300 * 1e300
assert str(x) == 'inf'
assert f'{x}' == 'inf'

assert '{:g}'.format(x) == 'inf'
assert '{:g}'.format(x * 0) == 'nan'

assert '{:G}'.format(x) == 'INF'
assert '{:G}'.format(x * 0) == 'NAN'

assert f'{x}' == 'inf'
assert f'{0 * x:g}' == 'nan'

assert f'{x:G}' == 'INF'
assert f'{0 * x:G}' == 'NAN'

# You’ll see similar behavior with the f and F presentations types as well:
assert '{:f}'.format(x) == 'inf'
assert '{:F}'.format(x) == 'INF'

assert '{:f}'.format(x * 0) == 'nan'
assert '{:F}'.format(x * 0) == 'NAN'

assert f'{x:f}' == 'inf'
assert f'{x:F}' == 'INF'

assert f'{0 * x:f}' == 'nan'
assert f'{0 * x:F}' == 'NAN'

# %	Percentage:
assert '%f%%' % 65.0 == '65.000000%'
assert '{:%}'.format(0.65) == '65.000000%'
p = 0.65
assert f'{p:%}' == '65.000000%'

# b	Binary integer
# e or E Exponential
# o	Octal integer

# The <fill> and <align> subcomponents control how formatted output is padded and positioned within the specified field
# width.

# Here are the possible values for the <align> subcomponent:
# <
# >
# ^
# =

assert '{0:<8s}'.format('foo') == 'foo     '
assert '{0:<8d}'.format(123) == '123     '
assert '{0:>8s}'.format('foo') == '     foo'
assert '{0:>8d}'.format(123) == '     123'
assert '{0:^8s}'.format('foo') == '  foo   '
assert '{0:^8d}'.format(123) == '  123   '

assert f'{"foo":<8s}' == 'foo     '
assert f'{123:<8d}' == '123     '
assert f'{"foo":>8s}' == '     foo'
assert f'{123:>8d}' == '     123'
assert f'{"foo":^8s}' == '  foo   '
assert f'{123:^8d}' == '  123   '

# Finally, you can also specify a value using the equals sign (=) for the <align> subcomponent. This only has meaning
# for numeric values, and only when a sign is included in the output.
assert '{0:+8d}'.format(123) == '    +123'
assert '{0:=+8d}'.format(123) == '+    123'
assert '{0:+8d}'.format(-123) == '    -123'
assert '{0:=+8d}'.format(-123) == '-    123'

assert f'{123:+8d}' == '    +123'
assert f'{123:=+8d}' == '+    123'
assert f'{-123:+8d}' == '    -123'
assert f'{-123:=+8d}' == '-    123'

# <fill> specifies how to fill in extra space when the formatted value doesn’t completely fill the output width.
assert '{0:->8s}'.format('foo') == '-----foo'
assert '{0:#<8d}'.format(123) == '123#####'
assert '{0:*^8s}'.format('foo') == '**foo***'

print(f'{"foo":->8s}')
assert f'{"foo":->8s}' == '-----foo'
assert f'{123:#<8d}' == '123#####'
assert f'{"foo":*^8s}' == '**foo***'

# You can control whether a sign appears in numeric output with the <sign> component. For example, in the following, the
# plus sign (+) specified in the <format_spec> indicates that the value should always be displayed with a leading sign:
assert '{0:+6d}'.format(123) == '  +123'
assert '{0:+6d}'.format(-123) == '  -123'

assert f'{123:+6d}' == '  +123'
assert f'{-123:+6d}' == '  -123'

# Here, you use the plus sign (+), so a sign will always be included for both positive and negative values.
# If you use the minus sign (-), then only negative numeric values will include a leading sign, and positive values
# won’t:
assert '{0:-6d}'.format(123) == '   123'
assert '{0:-6d}'.format(-123) == '  -123'

assert f'{123:-6d}' == '   123'
assert f'{-123:-6d}' == '  -123'

# When you use a single space (' '), it means a sign is included for negative values, and an ASCII space character for
# positive values:
assert '{0:*> 6d}'.format(123) == '** 123'
assert '{0:*> 6d}'.format(-123) == '**-123'
assert '{0:*>6d}'.format(123) == '***123'

assert f'{123:*> 6d}' == '** 123'
assert f'{-123:*> 6d}' == '**-123'
assert f'{123:*>6d}' == '***123'

# Since the space character is the default fill character, you’d only notice the effect of this if an alternate <fill>
# character is specified.

# The # Subcomponent
# For binary, octal, and hexadecimal presentation types, the hash character (#) causes inclusion of an explicit base
# indicator to the left of the value:
assert '{0:b}, {0:#b}'.format(16) == '10000, 0b10000'  # base indicator 0b
assert '{0:o}, {0:#o}'.format(16) == '20, 0o20'  # base indicator 0o
assert '{0:x}, {0:#x}'.format(16) == '10, 0x10'  # base indicator 0x

assert f'{16:b}, {16:#b}' == '10000, 0b10000'  # base indicator 0b
assert f'{16:o}, {16:#o}' == '20, 0o20'  # base indicator 0o
assert f'{16:x}, {16:#x}' == '10, 0x10'  # base indicator 0x

# For floating-point or exponential presentation types, the hash character forces the output to contain a decimal point,
# even if the output consists of a whole number:
assert '{0:.0f}, {0:#.0f}'.format(123) == '123, 123.'
assert '{0:.0e}, {0:#.0e}'.format(123) == '1e+02, 1.e+02'

assert f'{123:.0f}, {123:#.0f}' == '123, 123.'
assert f'{123:.0e}, {123:#.0e}' == '1e+02, 1.e+02'

# For any presentation type other than those shown above, the hash character (#) has no effect.

# The 0 Subcomponent
# If output is smaller than the indicated field width and you specify the digit zero (0) in <format_spec>, then values
# will be padded on the left with zeros instead of ASCII space characters:
assert '{0:05d}'.format(123) == '00123'
assert '{0:08.1f}'.format(12.3) == '000012.3'
assert '{0:>06s}'.format('foo') == '000foo'

assert f'{123:05d}' == '00123'
assert f'{12.3:08.1f}' == '000012.3'
assert f'{"foo":>06s}'.format('foo') == '000foo'

# If you specify both <fill> and <align>, then <fill> overrides 0:
assert '{0:*>05d}'.format(123) == '**123'

assert f'{123:*>05d}' == '**123'

# <fill> and 0 essentially control the same thing, so there really isn’t any need to specify both.

# The <width> Subcomponent
# <width> specifies the minimum width of the output field:
assert '{0:8s}'.format('foo') == 'foo     '
assert '{0:8d}'.format(123) == '     123'

assert f'{"foo":8s}' == 'foo     '
assert f'{123:8d}' == '     123'

# The <group> Subcomponent
# <group> allows you to include a grouping separator character in numeric output, which separates each group of three
# digits in the output:
assert '{0:,d}'.format(1234567) == '1,234,567'
assert '{0:_d}'.format(1234567) == '1_234_567'
assert '{0:,.2f}'.format(1234567.89) == '1,234,567.89'
assert '{0:_.2f}'.format(1234567.89) == '1_234_567.89'

assert f'{1234567:,d}' == '1,234,567'
assert f'{1234567:_d}' == '1_234_567'
assert f'{1234567.89:,.2f}' == '1,234,567.89'
assert f'{1234567.89:_.2f}' == '1_234_567.89'

# A <group> value using an underscore (_) may also be specified with the binary, octal, and hexadecimal presentation
# types. In that case, each group of four digits is separated by an underscore character in the output:
assert '{0:_b}'.format(0b111010100001) == '1110_1010_0001'
assert '{0:#_b}'.format(0b111010100001) == '0b1110_1010_0001'
assert '{0:_x}'.format(0xae123fcc8ab2) == 'ae12_3fcc_8ab2'
assert '{0:#_x}'.format(0xae123fcc8ab2) == '0xae12_3fcc_8ab2'

assert f'{0b111010100001:_b}' == '1110_1010_0001'
assert f'{0b111010100001:#_b}' == '0b1110_1010_0001'
assert f'{0xae123fcc8ab2:_x}' == 'ae12_3fcc_8ab2'
assert f'{0xae123fcc8ab2:#_x}' == '0xae12_3fcc_8ab2'

# If you try to specify <group> with any presentation type other than those listed above (, or _), then your code will
# raise an exception.

# The .<prec> Subcomponent
# .<prec> specifies the number of digits after the decimal point for floating point presentation types:
assert '{0:8.2f}'.format(1234.5678) == ' 1234.57'
assert '{0:8.4f}'.format(1.23) == '  1.2300'

assert '{0:8.2e}'.format(1234.5678) == '1.23e+03'
assert '{0:8.4e}'.format(1.23) == '1.2300e+00'

assert f'{1234.5678:8.2f}' == ' 1234.57'
assert f'{1.23:8.4f}' == '  1.2300'

assert f'{1234.5678:8.2e}' == '1.23e+03'
assert f'{1.23:8.4e}' == '1.2300e+00'

# For string types, .<prec> specifies the maximum width of the converted output:
assert '{:.4s}'.format('foobar') == 'foob'
# If the output would be longer than the value specified, then it will be truncated.
