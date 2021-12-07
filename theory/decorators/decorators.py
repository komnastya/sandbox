# https://realpython.com/primer-on-python-decorators/
import functools
from datetime import datetime


# DECORATORS

# A DECORATOR is a function that takes another function and extends the behavior of the latter function without
# explicitly modifying it.

# FIRST-CLASS OBJECTS

# In Python, functions are first-class objects. This means that functions can be passed around and used as arguments,
# just like any other object (string, int, float, list, and so on). Consider the following three functions:


def say_hello(name):
    return f"Hello {name}"


def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def greet_bob(some_func):
    return some_func("Bob")


assert greet_bob(say_hello) == "Hello Bob"


# Here, say_hello() and be_awesome() are regular functions that expect a name given as a string. The greet_bob()
# function however, expects a function as its argument.


# RETURNING FUNCTIONS FROM FUNCTIONS

# Python also allows you to use functions as return values. The following example returns one of the inner functions
# from the outer parent() function:

def parent(num):
    def first_child():
        return "Hi, I am Nastassia"

    def second_child():
        return "Call me George"

    if num == 1:
        return first_child
    else:
        return second_child


# Note that you are returning first_child without the parentheses. Recall that this means that you are returning
# a reference to the function first_child. In contrast first_child() with parentheses refers to the result of
# evaluating the function. This can be seen in the following example:

first = parent(1)
second = parent(2)

print(first, second,
      '\nThese are the links to the functions inside the parent function, which don\'t return any values')
print()

# In order to return the values, you need to call the function.

# You can now use first and second as if they are regular functions, even though the functions they point to can’t
# be accessed directly:

assert first() == "Hi, I am Nastassia"
assert second() == "Call me George"


# SIMPLE DECORATORS

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


def say_whee():
    print("Whee!")


say_whee = my_decorator(say_whee)

say_whee()
print()


# In effect, the name 'say_whee' now points to the wrapper() inner function. Remember that you return wrapper as
# a function when you call my_decorator(say_whee):

# >>> say_whee
# <function my_decorator.<locals>.wrapper at 0x7f3c5dfd42f0>

# However, wrapper() has a reference to the original say_whee() as func, and calls that function between the two calls
# to print().

# Put simply: DECORATORS WRAP A FUNCTION, MODIFYING ITS BEHAVIOR.

# The other example:
# Because wrapper() is a regular Python function, the way a decorator modifies a function can change dynamically. So as
# not to disturb your neighbors, the following example will only run the decorated code during the day:


def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep

    return wrapper


def say_whee():
    print("Whee!")


say_whee = not_during_the_night(say_whee)
print('Print not_during_the_night')
say_whee()
print()


# Syntactic Sugar

# Python allows you to use decorators in a simpler way with the @ symbol, sometimes called the “pie” syntax.
# The following example does the exact same thing as the first decorator example:

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_whee():
    print("Whee!")


print('Using @my_decorator')
say_whee()
print()


# So, @my_decorator is just an easier way of saying say_whee = my_decorator(say_whee). It’s how you apply a
# decorator to a function.


# REUSING DECORATORS

def do_twice(func):
    def wrapper_do_twice():
        func()
        func()

    return wrapper_do_twice


@do_twice
def hello():
    print('Hello!')


@do_twice
def hola():
    print("Hola!")


print('Using @do_twice with two different functions')
hello()
hola()
print()

# DECORATING FUNCTION WITH ARGUMENT
print('Decorating function with arguments')


# @do_twice
# def greeting(name):
#     print(f'Hello, {name}')
# greeting("Nastya") -> wrapper_do_twice() TypeError: takes 0 positional arguments but 1 was given (line 161)

# The problem is that the inner function wrapper_do_twice() does not take any arguments, but name="World" was passed
# to it. You could fix this by letting wrapper_do_twice() accept one argument, but then it would not work for the
# say_whee() function you created earlier.
# The solution is to use *args and **kwargs in the inner wrapper function.
# Then it will accept an arbitrary number of positional and keyword arguments.

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper_do_twice


# The wrapper_do_twice() inner function now accepts any number of arguments and passes them on to the function
# it decorates. Now both your say_whee() and greet() examples works:

@do_twice
def greeting(name):
    print(f'Hello, {name}!')


greeting('world')
hello()
print()


# RETURNING VALUES FROM DECORATED FUNCTION

# What happens to the return value of decorated functions? Well, that’s up to the decorator to decide. Let’s say you
# decorate a simple function as follows:
@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


print('Create greeting function with return statement:')
return_greeting('Nastya')
print()

print('Print this function:')
print(return_greeting('Nastya'))


# Oops, your decorator ate the return value from the function.
# Because the do_twice_wrapper() doesn’t explicitly return a value, the call return_greeting("Adam") ended up
# returning None.
# To fix this, you need to make sure the wrapper function returns the return value of the decorated function.

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


print('Add return statemant inside wapper_do_twice')
print(return_greeting('Nastya'))
print()
print("This is 'side effect' of assertion:")
assert return_greeting('Nastya') == 'Hi Nastya'

print()
print('Introspection:')
print(return_greeting)
print(return_greeting.__name__)
print(help(return_greeting))


# However, after being decorated, say_whee() has gotten very confused about its identity. It now reports being
# the wrapper_do_twice() inner function inside the do_twice() decorator. Although technically true, this is not very
# useful information.

# To fix this, decorators should use the @functools.wraps decorator, which will preserve information about
# the original function. Update decorator again:


def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice


# You do not need to change anything about the decorated say_whee() function:
@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


print()
print('Introspection:')
print(return_greeting)
print(return_greeting.__name__)
print(help(return_greeting))

# The @functools.wraps decorator uses the function functools.update_wrapper() to update special attributes
# like __name__ and __doc__ that are used in the introspection.
