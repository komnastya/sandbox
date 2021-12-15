from string import Template

errno = 50159747054
name = 'Nastya'
age = 26

# There are FOUR major ways to do string formatting in Python:

# #1 “Old Style” String Formatting (% Operator):
assert 'Hello, %s' % name == 'Hello, Nastya'

# You can use the %x format specifier to convert an int value to a string and to represent it as a hexadecimal number:
assert '%x' % errno == 'badc0ffee'
assert 'Hey %s, there is a 0x%x error!' % (name, errno) == 'Hey Nastya, there is a 0xbadc0ffee error!'

assert 'Hey %(name)s, there is a 0x%(errno)x error!' % {"name": name,
                                                        "errno": errno} == 'Hey Nastya, there is a 0xbadc0ffee error!'

# #2 “New Style” String Formatting (str.format):
assert 'Hello, {}!'.format(name) == 'Hello, Nastya!'
assert 'Hello, {1}! You are {0}.'.format(age, name) == 'Hello, Nastya! You are 26.'
assert 'Hello, {1}! {1}, you are {0} years old.'.format(age, name) == 'Hello, Nastya! Nastya, you are 26 years old.'
assert '{2}.{1}.{0}/{0}{0}.{1}{1}.{2}{2}'.format('foo', 'bar', 'baz') == 'baz.bar.foo/foofoo.barbar.bazbaz'
assert '{}{}'.format('foo', 'bar', 'baz') == 'foobar'
assert '{0}{x}{1}'.format('foo', 'bar', x='baz') == 'foobazbar'
assert 'Hey {name}, there is a 0x{errno:x} error!'.format(name=name,
                                                          errno=errno) == 'Hey Nastya, there is a 0xbadc0ffee error!'
person = {'name': 'Nastya', 'age': 26}
assert 'Hello, {name}! You are {age}.'.format(name=person['name'], age=person['age']) == 'Hello, Nastya! You are 26.'
assert 'Hello, {name}! You are {age}.'.format(**person) == 'Hello, Nastya! You are 26.'

# The following code uses string formatting with the str.format() function to pad a string with spaces:
assert '{:15}'.format('I am legend') == 'I am legend    '
assert '{:>15}'.format('I am legend') == '    I am legend'
assert '{:^15}'.format('I am legend') == '  I am legend  '

# #3 String Interpolation / f-Strings (Python 3.6+):
assert f'Hello, {name}!' == 'Hello, Nastya!'
assert f"Hey {name}, there's a {errno:#x} error!" == "Hey Nastya, there's a 0xbadc0ffee error!"

assert f'{{70 + 4}}' == '{70 + 4}'
assert f'{{{70 + 4}}}' == '{74}'
assert f'{{{{70 + 4}}}}' == '{{70 + 4}}'

# The following code uses string formatting with f-strings to pad the right end of a string with spaces:
width = 15
padding = ' '
assert f'{"I am legend" :{padding}<{width}}' == 'I am legend    '
assert f'{"I am legend" :{padding}>{width}}' == '    I am legend'
assert f'{"I am legend" :{padding}^{width}}' == '  I am legend  '

# #4 Template Strings (Standard Library):
t = Template('Hey, $name!')
assert t.substitute(name=name) == 'Hey, Nastya!'

# Another difference is that template strings don’t allow format specifiers. So in order to get the previous error
# string example to work, you’ll need to manually transform the int error number into a hex-string:

templ_string = 'Hey $name, there is a $error error!'
assert Template(templ_string).substitute(name=name, error=hex(errno)) == 'Hey Nastya, there is a 0xbadc0ffee error!'
