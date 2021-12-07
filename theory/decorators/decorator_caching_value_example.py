# https://realpython.com/primer-on-python-decorators/#more-real-world-examples
import functools

# CACHING RETURN VALUES

print('\nCaching return values:')


# Decorators can provide a nice mechanism for caching and memoization. As an example, let’s look at a recursive
# definition of the Fibonacci sequence:

def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1  # this is function attribute, which is assign outside of function
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)

    wrapper_count_calls.num_calls = 0  # assigning of the function 'num_calls' attribute
    return wrapper_count_calls


@count_calls
def fibonacci(num):  # counts the n-th number in fibonacci sequence
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


print(fibonacci(3))
print(fibonacci(5))


# To calculate the tenth Fibonacci number, you should really only need to calculate the preceding Fibonacci numbers,
# but this implementation somehow needs more calculations. It gets worse quickly: 21891 calculations are
# needed for fibonacci(20) and almost 2.7 million calculations for the 30th number. This is because the code keeps
# recalculating Fibonacci numbers that are already known.

# The usual solution is to implement Fibonacci numbers using a for loop and a lookup table. However, simple caching
# of the calculations will also do the trick:

def cache(func):
    """Keep a cache of previous function calls"""

    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())

        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]

    wrapper_cache.cache = dict()

    return wrapper_cache


@cache
@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 2) + fibonacci(num - 1)


# The cache works as a lookup table, so now fibonacci() only does the necessary calculations once:
print('\nUsing cache decorator:')
print('Fibonacci 5:', fibonacci(3))
print('Fibonacci 3:', fibonacci(3))
print('Fibonacci 10:', fibonacci(10))
