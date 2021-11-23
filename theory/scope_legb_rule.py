# https://realpython.com/python-scope-legb-rule
import sys
from functools import partial
from sys import platform


# PYTHON SCOPE & the LEGB RULE: RESOLVING NAMES IN YOUR CODE

# You can inspect the names and parameters of a function using .__code__, which is an attribute that holds information
# on the function’s internal code. Take a look at the code below:

def square(base):
    result = base ** 2
    return f'The square of {base} is: {result}'


print(square.__code__.co_argcount)
print(square.__code__.co_consts)
print(square.__code__.co_varnames)
print(square.__code__.co_name)

# In this code example, you inspect .__code__ on square(). This is a special attribute that holds information about
# the code of a Python function. In this case, you see that .co_varnames holds a tuple containing the names that you
# define inside square().

# MODIFYING THE BEHAVIOR OF A PYTHON SCOPE

# Even though Python scopes follow these general rules by default, there are ways to modify this standard behavior.
# Python provides two keywords that allow you to modify the content of global and nonlocal names. These two
# keywords are:

# 1. global
# 2. nonlocal

# The GLOBAL statement
gl_counter = 50


def update_counter():
    global gl_counter  # Declare gl_counter as global
    gl_counter = gl_counter + 10


update_counter()
update_counter()
assert gl_counter == 70


# With the statement global counter, you’re telling Python to look in the global scope for the name counter. This way,
# the expression counter = counter + 1 doesn’t create a new name in the function scope, but updates it in the
# global scope.

# Note: The use of global is considered bad practice in general. If you find yourself using global to fix problems
# like the one above, then stop and think if there is a better way to write your code.

# For example, you can try to write a self-contained function that relies on local names rather than on global
# names as follows:

def update_counter_2(counter):
    return counter + 1


gl_counter = update_counter_2(gl_counter)
gl_counter = update_counter_2(gl_counter)
gl_counter = update_counter_2(gl_counter)

assert gl_counter == 73


# You can also use a global statement to create lazy global names by declaring them inside a function. Take a
# look at the following code:

def create_lazy_name():
    global lazy  # Create a global var, lazy
    lazy = 15
    return lazy


assert create_lazy_name() == 15
assert lazy == 15


# The NONLOCAL statement

# The nonlocal statement consists of the nonlocal keyword followed by one or more names separated by commas. These
# names will refer to the same names in the enclosing Python scope. The following example shows how you can use
# nonlocal to modify a variable defined in the enclosing or nonlocal scope:

def func():
    var = 100

    def nested():
        nonlocal var
        var += 100

    nested()
    return var


assert func() == 200


# Unlike global, you can’t use nonlocal outside of a nested or enclosed function. To be more precise, you can’t use
# a nonlocal statement in either the global scope or in a local scope.

# In contrast to global, you can’t use nonlocal to create lazy nonlocal names. Names must already exist in the
# enclosing Python scope if you want to use them as nonlocal names. This means that you can’t create nonlocal names
# by declaring them in a nonlocal statement in a nested function. Take a look at the following code example:

# >>> def func():
# ...     def nested():
# ...         nonlocal lazy_var  # Try to create a nonlocal lazy name
# SyntaxError: no binding for nonlocal 'lazy_var' found -> because lazy_var doesn’t exist in the enclosing scope
# of nested().


# USING ENCLOSING SCOPE AS CLOSURES

# Closures provide a way to retain state information between function calls. This can be useful when you want to write
# code based on the concept of lazy or delayed evaluation. Take a look at the following code for an example of how
# closures work and how you can take advantage of them in Python:

def power_factory(exp):
    def power_of(base):
        return base ** exp

    return power_of


square_of = power_factory(2)
cube_of = power_factory(3)

assert square_of(2) == 4
assert square_of(3) == 9
assert cube_of(2) == 8
assert cube_of(3) == 27


# In the above example, the inner function power() is first assigned to square. In this case, the function remembers
# that exp equals 2. In the second example, you call power_factory() using 3 as an argument. This way, cube holds a
# function object, which remembers that exp is 3. Notice that you can freely reuse square and cube because they don’t
# forget their respective state information.

def mean():
    sample = []

    def _mean(number):
        sample.append(number)
        return sum(sample) / len(sample)

    return _mean


add_data = mean()
assert add_data(5) == 5  # [5] -> 5/1 = 5
assert add_data(7) == 6  # [5, 7] -> (5 + 7) / 2 = 6
assert add_data(9) == 7  # [5, 7, 9] -> (5 + 7 + 9) / 3 = 7


# The closure that you create in the above code remembers the state information of sample between calls of current_mean.

# Notice that if your data stream gets too large, then this function can become a problem in terms of memory usage.
# That’s because with each call to 'add_data', 'sample' will hold a bigger and bigger list of values. Take a look at
# the following code for an alternative implementation using nonlocal:

def mean_two():
    total = 0
    length = 0

    def _mean(number):
        nonlocal total, length
        total += number
        length += 1
        return total / length

    return _mean


add_data_better_way = mean_two()
assert add_data_better_way(2) == 2  # [2] -> 2/1 = 2
assert add_data_better_way(4) == 3  # [2, 4] -> (2 + 4) / 2 = 3
assert add_data_better_way(6) == 4  # [2, 4, 6] -> (2 + 4 + 6) / 3 = 4


# Even though this solution is more verbose, you don’t have an endlessly growing list anymore. You now have a single
# value for total and length. This implementation is a lot more efficient in terms of memory consumption than the
# previous solution.

# Finally, you can find some examples of using closures in the Python standard library. For example, functools
# provides a function named partial() that makes use of the closure technique to create new function objects that can
# be called using predefined arguments. Here’s an example:

# Partial functions allow us to fix a certain number of arguments of a function and generate a new function.
# A normal function
def f(a, b, c, x):
    return 1000 * a + 100 * b + 10 * c + x


# A partial function that calls f with a as 3, b as 1 and c as 4.
g = partial(f, 3, 1, 4)

# Calling g()
assert g(5) == 3145


# You use partial to build a function object that remembers the state information, where exp=2. Then, you call this
# object to perform the power operation and get the final result.
def power(exp, base):
    return base ** exp


square = partial(power, 2)
assert square(2) == 4
assert square(10) == 100

# DISCOVERING UNUSUAL PYTHON SCOPES

# You’ll find some Python structures where name resolution seems not to fit into the LEGB rule for Python scopes.
# These structures include:

# 1. Comprehensions
# 2. Exception blocks
# 3. Classes and instances

# In the next few sections, you’ll cover how Python scope works on these three structures. With this knowledge, you’ll
# be able to avoid subtle errors related to the use of names in these kinds of Python structures.

# 1 COMPREHENSION VARIABLE SCOPES

lst = [item for item in range(5)]
assert lst == [0, 1, 2, 3, 4]

# print(item) raise NameError

# Once you run the list comprehension, the variable item is forgotten and you can’t access its value anymore. It’s
# unlikely that you need to use this variable outside of the comprehension, but regardless, Python makes sure that
# its value is no longer available once the comprehension finishes.

# Note that this only applies to comprehensions. When it comes to regular for loops, the loop variable holds the last
# value processed by the loop:

stack = []
for item in range(5):
    stack.append(item)

assert item == 4
# You can freely access the loop variable item once the loop has finished. Here, the loop variable holds the last
# value processed by the loop, which is 4 in this example.


# EXCEPTION VARIABLES SCOPE

# The exception variable is a variable that holds a reference to the exception raised by a try statement.
# In Python 3.x, such variables are local to the except block and are forgotten when the block ends. Check out the
# following code:

lst = [1, 2, 3]
try:
    lst[4]
except IndexError as err:
    # The variable err is local to this block
    # Here you can do anything with err
    print(err)


# print(err) err  -- > NameError: name 'err' is not defined

# err holds a reference to the exception raised by the try clause. You can use err only inside the code block of the
# except clause. This way, you can say that the Python scope for the exception variable is local to the except
# code block. Also note that if you try to access err from outside the except block, then you’ll get a NameError.
# That’s because once the except block finishes, the name doesn’t exist anymore.


# CLASS AND INSTANCE ATTRIBUTES SCOPE

# When you define a class, you’re creating a new local Python scope. The names assigned at the top level of the class
# live in this local scope. The names that you assigned inside a class statement don’t clash with names elsewhere.
# You can say that these names follow the LEGB rule, where the class block represents the L level.

# Unlike functions, the class local scope isn’t created at call time, but at execution time. Each class object has
# its own .__dict__ attribute that holds the class scope or namespace where all the class attributes live.
# Check out this code:

class A:
    attr = 100


print(A.__dict__.keys())

# To get access to a class attribute from outside the class, you need to use the dot notation as follows:
assert A.attr == 100

# Whenever you call a class, you’re creating a new instance of that class. Instances have their own .__dict__ attribute
# that holds the names in the instance local scope or namespace. These names are commonly called instance attributes
# and are local and specific to each instance. This means that if you modify an instance attribute, then the changes
# will be visible only to that specific instance.

a_obj = A()
b_obj = A()
assert a_obj.attr == 100
assert b_obj.attr == 100

b_obj.attr = 200
assert a_obj.attr == 100
assert b_obj.attr == 200


# You can override a class attribute with an instance attribute, which will modify the general behavior of your class.
# However, you can access both attributes unambiguously using the dot notation like in the following example:
class B:
    var = 100

    def __init__(self):
        self.var = 200

    def access_attr(self):
        # Use dot notation to access class and instance attributes
        print(f'The instance attribute is: {self.var}')
        print(f'The class attribute is: {B.var}')


obj = B()
assert B.var == 100
assert B().var == 200
assert obj.var == 200
obj.var = 300
assert obj.var == 300
assert B().var == 200
print(B.__dict__.keys())
print(obj.__dict__.keys())

# USING SCOPE RELATED BUILT-IN FUNCTIONS

# There are many built-in functions that are closely related to the concept of Python scope and namespaces.
# In previous sections, you’ve used dir() to get information on the names that exist in a given scope.
# Besides dir(), there are some other built-in functions that can help you out when you’re trying to get
# information about a Python scope or namespace. In this section, you’ll cover how to work with:

# 1 globals()
# 2 locals()
# 3 dir()
# 4 vars()

# 1 GLOBALS

# In Python, globals() is a built-in function that returns a reference to the current global scope or namespace
# dictionary. This dictionary always stores the names of the current module. This means that if you call globals() in
# a given module, then you’ll get a dictionary containing all the names that you’ve defined in that module, right
# before the call to globals().
print(globals())


# An interesting example of how you can use globals() in your code would be to dynamically dispatch functions that
# live in the global scope. Suppose you want to dynamically dispatch platform-dependent functions. To do this, you
# can use globals() as follows:

def linux_print():
    return 'Printing from Linux...'


def win32_print():
    return 'Printing from Windows...'


def darwin_print():
    return 'Printing from macOS...'


printer = globals()[platform + '_print']
assert printer() == 'Printing from Windows...'

# Another example of how to use globals() would be to inspect the list of special names in the global scope.
# Take a look at the following list comprehension:
print("Globals which started with __ :", [name for name in globals() if name.startswith('__')])

# Note that you can use the globals() dictionary just like you would use any regular dictionary. For example, you
# can iterate through it through it using these traditional methods:

# .keys()
# .values()
# .items()

# You can also perform regular subscription operations over globals() by using square brackets like in
# globals()['name']. For example, you can modify the content of globals() even though this isn’t recommended.
# Take a look at this example:
assert __doc__ is None
globals()['__doc__'] = """Docstring for __main__."""
assert __doc__ == 'Docstring for __main__.'

# 2 LOCALS

# locals()
# Another function related to Python scope and namespaces is locals(). This function updates and returns a dictionary
# that holds a copy of the current state of the local Python scope or namespace. When you call locals() in a function
# block, you get all the names assigned in the local or function scope up to the point where you call locals().
# Here’s an example:

def func(arg):
    var = 100
    print("Locals for func", locals())
    another = 200
    print(locals() is globals())


func(300)

# If you call locals() in the global Python scope, then you’ll get the same dictionary that you would get
# if you were to call globals().
assert locals() is globals()


# Note that you shouldn’t modify the content of locals() because changes may have no effect on the values of local
# and free names. Check out the following example:
def func():
    var = 100
    locals()['var'] = 200
    return var


assert func() == 100

# 3 VARS()

# vars() is a Python built-in function that returns the .__dict__ attribute of a module, class, instance, or any
# other object which has a dictionary attribute. Remember that .__dict__ is a special dictionary that Python uses
# to implement namespaces. Take a look at the following examples:

# print(vars(sys)) # With a module object
assert vars(sys) is sys.__dict__


class MyClass:
    def __init__(self, var):
        self.var = var


obj = MyClass(100)
print("Object vars: ", vars(obj))  # With a user-defined object
print("Class vars: ", vars(MyClass))  # With a class

# Without any argument, vars() acts like locals() and returns a dictionary with all the names in the local Python scope:
assert vars() is locals()


# If you call vars() with an object that doesn’t have a .__dict__, then you’ll get a TypeError => if you call vars()
# with an integer object, then you’ll get a TypeError because this type of Python object doesn’t have a .__dict__.

# 4 DIR()

# You can use dir() without arguments to get the list of names in the current Python scope. If you call dir() with an
# argument, then the function attempts to return a list of valid attributes for that object.

# If you call dir() with no arguments, then you get a list containing the names that live in the global scope. You
# can also use dir() to inspect the list of names or attributes of different objects. This includes functions, modules,
# variables, and so on.

# Even though the official documentation says that dir() is intended for interactive use, you can use the function
# to provide a comprehensive list of attributes of a given object. Note that you can also call dir() from inside a
# function. In this case, you’ll get the list of names defined in the function scope.

def func():
    var = 100
    print(dir())
    another = 200  # Is defined after calling dir()


func()

# In this example, you use dir() inside func(). When you call the function, you get a list containing the names that
# you define in the local scope. It’s worth noting that in this case, dir() only shows the names you declared
# before the function call.
