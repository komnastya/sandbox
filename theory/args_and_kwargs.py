# https://realpython.com/python-kwargs-and-args/

# PYTHON ARGS AND KWARGS

# PASSING MULTIPLE ARGUMENTS TO A FUNCTION

# *args and **kwargs allow you to pass multiple arguments or keyword arguments to a function. Consider the following
# example. This is a simple function that takes two arguments and returns their sum:

def my_sum(a, b):
    return a + b


assert my_sum(1, 2) == 3


# This function works fine, but it’s limited to only two arguments. What if you need to sum a varying number of
# arguments, where the specific number of arguments passed is only determined at runtime? Wouldn’t it be great to
# create a function that could sum all the integers passed to it, no matter how many there are?

# USING THE PYTHON ARGS VARIABLE IN FUNCTION DEFINITIONS

# There are a few ways you can pass a varying number of arguments to a function. The first way is often the most
# intuitive for people that have experience with collections. You simply pass a list or a set of all the arguments
# to your function. So for my_sum(), you could pass a list of all the integers you need to add:

def my_sum2(my_integers):
    result = 0
    for x in my_integers:
        result += x
    return result


list_of_integers = [1, 2, 3]
assert my_sum2(list_of_integers) == 6


# This implementation works, but whenever you call this function you’ll also need to create a list of arguments to
# pass to it. This can be inconvenient, especially if you don’t know up front all the values that should go into
# the list.

# This is where *args can be really useful, because it allows you to pass a varying number of positional arguments.
# Take the following example:

def my_sum3(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result


assert my_sum3(1, 3, 5) == 9


# In this example, you’re no longer passing a list to my_sum(). Instead, you’re passing three different positional
# arguments. my_sum() takes all the parameters that are provided in the input and packs them all into a single iterable
# object named args.

# Note that args is just a name. You’re not required to use the name args. You can choose any name that you prefer,
# such as integers:

# def my_sum(*integers):
#     result = 0
#     for x in integers:
#         result += x
#     return result

# The function still works, even if you pass the iterable object as integers instead of args. All that matters here
# is that you use the unpacking operator (*).
# Bear in mind that the iterable object you’ll get using the unpacking operator * is not a list but a tuple.

# USING THE PYTHON KWARGS VARIABLE IN FUNCTION DEFINITION

# **kwargs works just like *args, but instead of accepting positional arguments it accepts keyword (or named) arguments.
# Take the following example:

def concatenate(**kwargs):
    result = ""
    for arg in kwargs.values():
        result += arg
    return result


assert concatenate(a="Real ", b="Python ", c="Is ", d="Great", e="!") == "Real Python Is Great!"


# Like args, kwargs is just a name that can be changed to whatever you want. Again, what is important here is the use
# of the unpacking operator (**).

# So, the previous example could be written like this:
# def concatenate(**words):
#     result = ""
#     for arg in words.values():
#         result += arg
#     return result

# Note that in the example above the iterable object is a standard dict. If you iterate over the dictionary and want
# to return its values, like in the example shown, then you must use .values().

# In fact, if you forget to use this method, you will find yourself iterating through the keys of your Python kwargs
# dictionary instead, like in the following example:

def concatenate_keys(**kwargs):
    result = ""
    # Iterating over the keys of the Python kwargs dictionary
    for arg in kwargs:
        result += arg
    return result


assert concatenate_keys(a="Real", b="Python", c="Is", d="Great", e="!") == "abcde"


# ORDERING ARGUMENTS IN A FUNCTIONS

# Now that you have learned what *args and **kwargs are for, you are ready to start writing functions that take a
# varying number of input arguments. But what if you want to create a function that takes a changeable number of both
# positional and named arguments?

# In this case, you have to bear in mind that order counts. Just as non-default arguments have to precede default
# arguments, so *args must come before **kwargs.

# To recap, the correct order for your parameters is:

# 1 Standard arguments
# 2 *args arguments
# 3 **kwargs arguments

# For example, this function definition is correct:

def correct_function_definition(a, b, *args, **kwargs):
    pass


# The *args variable is appropriately listed before **kwargs. But what if you try to modify the order of the arguments?
# For example, consider the following function:

# def wrong_function_definition(a, b, **kwargs, *args):
#     pass

# Now, **kwargs comes before *args in the function definition. If you try to run this example, you’ll receive an error
# from the interpreter:
# $ python wrong_function_definition.py
#   File "wrong_function_definition.py", line 2
#     def my_function(a, b, **kwargs, *args):
# SyntaxError: invalid syntax

# In this case, since *args comes after **kwargs, the Python interpreter throws a SyntaxError.


# UNPACKING WITH THE ASTERISK OPERATORS: * and **

# The single and double asterisk unpacking operators were introduced in Python 2. In short, the unpacking operators
# are operators that unpack the values from iterable objects in Python. The single asterisk operator * can be used on
# any iterable that Python provides, while the double asterisk operator ** can only be used on dictionaries.

# Let’s start with an example:

my_list = [1, 2, 3]
assert my_list == [1, 2, 3]

print('Note the difference how the lists are printed:')
print(my_list)

# Here, the * operator tells print() to unpack the list first. In this case, the output is no longer the list itself,
# but rather the content of the list:
print(*my_list)


# Can you see the difference between this execution and the one from print_list.py? Instead of a list, print() has
# taken three separate arguments as the input.

# Another thing you’ll notice is that you used the unpacking operator * to call a function, instead of in a function
# definition. In this case, print() takes all the items of a list as though they were single arguments.

# You can also use this method to call your own functions, but if your function requires a specific number of arguments,
# then the iterable you unpack must have the same number of arguments.

# To test this behavior, consider this script:

def my_sum4(a, b, c):
    return a + b + c


lst = [1, 2, 3]
assert my_sum4(*lst) == 6


# Here, my_sum() explicitly states that a, b, and c are required arguments.
# The 3 elements in lst match up perfectly with the required arguments in my_sum4().

# Now look at the following script, where my_list has 4 arguments instead of 3:
# def my_sum(a, b, c):
#     print(a + b + c)

# my_list = [1, 2, 3, 4]
# my_sum(*my_list)

# In this example, my_sum() still expects just three arguments, but the * operator gets 4 items from the list. If you
# try to execute this script, you’ll see that the Python interpreter is unable to run it:
# >>> TypeError: my_sum() takes 3 positional arguments but 4 were given

# When you use the * operator to unpack a list and pass arguments to a function, it’s exactly as though you’re passing
# every single argument alone. This means that you can use multiple unpacking operators to get values from several
# lists and pass them all to a single function.

# To test this behavior, consider the following example:

def my_sum5(*args):
    result = 0
    for x in args:
        result += x
    return result


lst1 = [1, 2, 3]
lst2 = [4, 5]
lst3 = [6, 7, 8, 9]

assert my_sum5(*lst1, *lst2, *lst3) == 45

# In this example all three lists are unpacked. Each individual item is passed to my_sum5()

# There are other convenient uses of the unpacking operator. For example, say you need to split a list into three
# different parts. The output should show the first value, the last value, and all the values in between. With the
# unpacking operator, you can do this in just one line of code:

lst5 = [1, 2, 3, 4, 5, 6]

a, *b, c = lst5
assert a == (1)
assert b == [2, 3, 4, 5]
assert c == (6)

# Another interesting thing you can do with the unpacking operator * is to split the items of any iterable object.
# This could be very useful if you need to merge two lists, for instance:
first_list = [1, 2, 3]
second_list = [4, 5, 6]
merged_list = [*first_list, *second_list]

assert merged_list == [1, 2, 3, 4, 5, 6]

# You can even merge two different dictionaries by using the unpacking operator **:

first_dict = {"A": 1, "B": 2}
second_dict = {"C": 3, "D": 4}
merged_dict = {**first_dict, **second_dict}

assert merged_dict == {"A": 1, "B": 2, "C": 3, "D": 4}

# Remember that the * operator works on any iterable object. It can also be used to unpack a string:

a = [*"RealPython"]
assert a == ['R', 'e', 'a', 'l', 'P', 'y', 't', 'h', 'o', 'n']

# The previous example seems great, but when you work with these operators it’s important to keep in mind the seventh
# rule of The Zen of Python by Tim Peters: Readability counts.

# To see why, consider the following example:
*a, = 'RealPython'

# There’s the unpacking operator *, followed by a variable, a comma, and an assignment. That’s a lot packed into
# one line! In fact, this code is no different from the previous example. It just takes the string RealPython and
# assigns all the items to the new list a, thanks to the unpacking operator *.

# The comma after the a does the trick. When you use the unpacking operator with variable assignment, Python requires
# that your resulting variable is either a list or a tuple. With the trailing comma, you have defined a tuple with
# only one named variable, a, which is the list ['R', 'e', 'a', 'l', 'P', 'y', 't', 'h', 'o', 'n'].
assert a == ['R', 'e', 'a', 'l', 'P', 'y', 't', 'h', 'o', 'n']

# You never get to see the tuple that Python creates in this operation, because you use tuple unpacking in combination
# with the unpacking operator *.

# If you name a second variable on the left-hand side of the assignment, Python will assign the last character of the
# string to the second variable, while collecting all remaining characters in the list a:

*a, b = "RealPython"
assert a == ['R', 'e', 'a', 'l', 'P', 'y', 't', 'h', 'o']
assert b == 'n'
