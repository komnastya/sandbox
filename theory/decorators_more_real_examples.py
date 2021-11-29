# https://realpython.com/primer-on-python-decorators/#more-real-world-examples
import functools
import time

# DECORATORS: MORE REAL WORLDS EXAMPLES

# SLOWING DOWN CODE, Revisited

print('\nSlowing code down with and without arguments: ')


def slow_down_initial(func):
    """Sleep 1 second before calling the function"""

    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)

    return wrapper_slow_down


@slow_down_initial
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)


# As noted earlier, our previous implementation of @slow_down always sleeps for one second. Now you know how to add
# parameters to decorators, so let’s rewrite @slow_down using an optional rate argument that controls how long it
# sleeps:

def slow_down_new(_func=None, *, rate=1):
    """Sleep given amount of seconds before calling the function"""

    def decorator_slow_down(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(rate)
            return func(*args, **kwargs)

        return wrapper

    if _func is None:
        return decorator_slow_down
    else:
        return decorator_slow_down(_func)


def countdown_new_without(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown_new_without(from_number - 1)


print('Without decorator:')
slow_down_new(rate=2)(countdown_new_without)(3)
slow_down_new(countdown_new_without)(3)

print('\nWith decorator:')


@slow_down_new(rate=3)
def countdown_new(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)


countdown_new(5)


# CREATE SINGLETON

print('\nCreate singleton:')


# A singleton is a class with only one instance. There are several singletons in Python that you use frequently,
# including None, True, and False. It is the fact that None is a singleton that allows you to compare for None
# using the is keyword.

# Using IS returns TRUE only for objects that are the exact same instance. The following @singleton decorator turns
# a class into a singleton by storing the first instance of the class as an attribute. Later attempts at creating an
# instance simply return the stored instance.

def singleton(cls):
    """Make a class a Singleton class (only one instance)"""

    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance

    wrapper_singleton.instance = None
    return wrapper_singleton


# As you see, this class decorator follows the same template as our function decorators. The only difference is that
# we are using cls instead of func as the parameter name to indicate that it is meant to be a class decorator.

@singleton
class TheOne:
    pass


first_one = TheOne()
another_one = TheOne()

assert id(first_one) == id(another_one)
assert first_one is another_one

print('First_one id:', id(first_one))
print('Another_one id:', id(another_one))

# It seems clear that first_one is indeed the exact same instance as another_one.

# Note: Singleton classes are not really used as often in Python as in other languages. The effect of a singleton
# is usually better implemented as a global variable in a module.
