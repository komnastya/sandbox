# Python keywords

# The WITH keyword

# Context managers are a really helpful structure in Python. Each context manager executes specific code before
# and after the statements you specify. To use one, you use the with keyword:

# with <context manager> as <var>:
#     <statements>

# WITH statement is used to wrap the execution of a block of code within methods defined by the context manager.
# Context manager is a class that implements __enter__ and __exit__ methods. Use of WITH statement ensures that
# the __exit__ method is called at the end of the nested block. This concept is similar to the use of try…finally block.

# If you wanted to open a file, do something with that file, and then make sure that the file was closed correctly,
# then you would use a context manager. Consider this example in which names.txt contains a list of names, one per line:

with open("names.txt") as input_file:
    for name in input_file:
        print(name.strip())

# The file I/O context manager provided by open() and initiated with the WITH keyword opens the file for reading,
# assigns the open file pointer to input_file, then executes whatever code you specify in the WITH block.
# Then, after the block is executed, the file pointer closes. Even if your code in the WITH block raises an exception,
# the file pointer would still close.

# The AS keyword uses with WITH

# AS is used to create an alias while importing a module. It means giving a different name (user-defined) to a module
# while importing it.

#  You may have also seen as used to alias imports and exceptions, and this is no different. The alias is available
#  in the with block:

# with <expr> as <alias>:
#     <statements>

# Most of the time, you’ll see these two Python keywords, with and as, used together.
# Examples:

# import math as mathematics
# import functools as tools
# import lambda_test as test_module
# from lambda_test import test_l_func_natural_number as test_func

# The ASSERT keywords

# ASSERT is used for debugging purposes.

# While programming, sometimes we wish to know the internal state or check if our assumptions are true. ASSERT helps
# us do this and find bugs more conveniently. ASSERT is followed by a condition.

# If the condition is true, nothing happens. But if the condition is false, AssertionError is raised. For example:

a = 4
assert a < 5
# assert a > 5 -> AssertionError

# For our better understanding, we can also provide a message to be printed with the AssertionError.

# assert a > 5, "The value of a is too small" -> AssertionError: The value of a is too small

# At this point we can note that, assert condition, message is equivalent to:

# if not condition:
#     raise AssertionError(message)


# ASYNC
# AWAIT
