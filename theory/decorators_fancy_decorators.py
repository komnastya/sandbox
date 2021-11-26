# https://realpython.com/primer-on-python-decorators/#fancy-decorators
import functools
import time


# DECORATING CLASSES

# There are two different ways you can use decorators on classes. The first one is very close to what you have
# already done with functions: you can decorate the methods of a class. This was one of the motivations for
# introducing decorators back in the day.

# Some commonly used decorators that are even built-ins in Python are @classmethod, @staticmethod, and @property.
# The @classmethod and @staticmethod decorators are used to define methods inside a class namespace that are NOT
# connected to a particular instance of that class. The @property decorator is used to customize getters and setters
# for class attributes.

# Let’s define a class where we decorate some of its methods using the @debug and @timer decorators:

def debug(func):
    """Print the function signature and return value"""

    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]  # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)  # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")  # 4
        return value

    return wrapper_debug


def timer(func):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper_time(*args, **kwargs):
        start_time = time.perf_counter()  # 1
        value = func(*args, *kwargs)
        end_time = time.perf_counter()  # 2
        run_time = end_time - start_time  # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_time


class TimeWaster:
    @debug
    def __init__(self, max_num):
        self.max_num = max_num

    @timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i ** 2 for i in range(self.max_num)])


# Using this class, you can see the effect of the decorators:
print("\nSee the effect of timer decorator to the init and the waste_time methods:\n")
tw = TimeWaster(1000)
tw.waste_time(50)
tw.waste_time(250)


# The other way to use decorators on classes is to decorate the whole class. This is, for example, done in the new
# dataclasses module in Python 3.7:

# from dataclasses import dataclass

# @dataclass
# class PlayingCard:
#     rank: str
#     suit: str

# The meaning of the syntax is similar to the function decorators. In the example above, you could have done the
# decoration by writing PlayingCard = dataclass(PlayingCard).

# Writing a class decorator is very similar to writing a function decorator. The only difference is that the decorator
# will receive a class and not a function as an argument. In fact, the decorators you saw above will work as class
# decorators. When you are using them on a class instead of a function, their effect might not be what you want.
# In the following example, the @timer decorator is applied to a class:

@timer
class TimeWaster_two:
    def __init__(self, max_num):
        self.max_num = max_num

    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i ** 2 for i in range(self.max_num)])


# Decorating a class does not decorate its methods. Recall that @timer is just shorthand
# for TimeWaster_two = timer(TimeWaster_two).

# Here, @timer only measures the time it takes to instantiate the class:
print("\nSee the effect of timer decorator to the whole class:\n")
tw = TimeWaster_two(2500)
tw.waste_time(99)


# NESTING DECORATORS

# You can apply several decorators to a function by stacking them on top of each other:

def do_twice(func):
    @functools.wraps(func)
    def wrap_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrap_do_twice


@debug
@do_twice
def greet(name):
    print(f"Hello, {name}")


# Think about this as the decorators being executed in the order they are listed. In other words, @debug calls
# @do_twice, which calls greet(), or debug(do_twice(greet())):
print('\nUsing of two decorators:\n')
greet('Eva')

# Observe the difference if we change the order of @debug and @do_twice.
# In this case, @do_twice will be applied to @debug as well:

print('\nChange the order of two decorators:\n')


@do_twice
@debug
def greet_two(name):
    print(f"Hello, {name}")


greet_two('Bob')

# DECORATORS WITH ARGUMENTS

# Sometimes, it’s useful to pass arguments to your decorators. For instance, @do_twice could be extended to a
# @repeat(num_times) decorator. The number of times to execute the decorated function could then be given as an
# argument.

print('\nDecorators with arguments:')


def repeat(num_times):  # this is a decorator factory, a funciton which creates decorators
    def decorator_repeat(func):  # this is the new decorator created by the factory
        @functools.wraps(func)  # this is the funciton returned by the decorator
        def wrap_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value

        return wrap_repeat

    return decorator_repeat


def greet_three(name):
    print(f'Hello, {name}!')


# How it works without decorator property:

four_times = repeat(4)  # this is the link to the inner decorator - decorator_repeat
decorator = four_times(greet_three)  # but the decorator property rewrite the function original name, so

four_times = four_times(greet_three)  # this is the link to the wrap_repeat function
four_times('Nastassia')  # here we call wrap_repeat function


# We can do the same using the decorator with argument(s):

@repeat(num_times=2)
def hooray(name):
    print(f'Hooray! {name} has understood it!')


hooray('Nastya')
