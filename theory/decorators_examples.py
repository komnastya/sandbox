# https://realpython.com/primer-on-python-decorators/#a-few-real-world-examples
import functools
import math
import random
import time


# A FEW REAL WORD EXAMPLES

# Let’s look at a few more useful examples of decorators. You’ll notice that they’ll mainly follow the same pattern
# that you’ve learned so far:


def decorator_pattern(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value

    return wrapper_decorator


# This formula is a good boilerplate template for building more complex decorators.

# Example #1: TIMING FUNCTION
# Let’s start by creating a @timer decorator. It will measure the time a function takes to execute and print the
# duration to the console.
# duration to the console.
print('Timing function\n')


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


@timer
def waste_some_time(num_times):
    a = 0
    for _ in range(num_times):
        a = sum([i ** 2 for i in range(1000)])
    print(a)


# This decorator works by storing the time just before the function starts running (at the line marked # 1) and
# just after the function finishes (at # 2). The time the function takes is then the difference between the two
# (at # 3). We use the time.perf_counter() function, which does a good job of measuring time intervals. Here are
# some examples of timings:

waste_some_time(1)
waste_some_time(10)
waste_some_time(100)
waste_some_time(500)

# Example #2: DEBUGGING CODE
print('\nDebugging code\n')


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


@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Hello, {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"


make_greeting('Nastassia', 26)
make_greeting('George', 11)

print('\nUsing "print" statement\n')
print(make_greeting('George', 11))

# This example might not seem immediately useful since the @debug decorator just repeats what you just wrote. It’s
# more powerful when applied to small convenience functions that you don’t call directly yourself.

# The following example calculates an approximation to the mathematical constant e:

math.factorial = debug(math.factorial)


def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))


print('\nFind approximate E\n')
print(approximate_e(5))

# Example #3: SLOWING DOWN CODE
print('\nSLowing down code\n')


# This next example might not seem very useful. Why would you want to slow down your Python code? Probably the most
# common use case is that you want to rate-limit a function that continuously checks whether a resource—like a web
# page—has changed. The @slow_down decorator will sleep one second before it calls the decorated function:

def slow_down(func):
    """Sleep one second before calling the function"""

    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)

    return wrapper_slow_down


@slow_down
def countdown(number):
    if number < 1:
        print('Light off')
    else:
        print(number)
        countdown(number - 1)


countdown(3)

# Example #4: REGISTERING PLUGINS
print('\nRegistering plugins\n')

PLUGINS = dict()


def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func


@register
def say_hello(name):
    return f'Hello, {name}!'


@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesome!"


def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)


# The @register decorator simply stores a reference to the decorated function in the global PLUGINS dict. Note that
# you do not have to write an inner function or use @functools.wraps in this example because you are returning the
# original function unmodified.

# The randomly_greet() function randomly chooses one of the registered functions to use. Note that the PLUGINS
# dictionary already contains references to each function object that is registered as a plugin:
print("PLUGINS dict:", PLUGINS)

print(randomly_greet("Nastassia"))

# The main benefit of this simple plugin architecture is that you do not need to maintain a list of which plugins
# exist. That list is created when the plugins register themselves. This makes it trivial to add a new plugin: just
# define the function and decorate it with @register.

#  If you are familiar with globals() in Python, you might see some similarities to how the plugin architecture works.
#  globals() gives access to all global variables in the current scope, including your plugins.

# Using the @register decorator, you can create your own curated list of interesting variables, effectively
# hand-picking some functions from globals().
