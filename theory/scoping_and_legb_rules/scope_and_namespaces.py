# https://realpython.com/python-namespaces-scope/
import builtins

# NAMESPACES AND SCOPE IN PYTHON

# In a Python program, there are four types of namespaces:

# 1 Built-In
# 2 Global
# 3 Enclosing
# 4 Local
# These have differing lifetimes. As Python executes a program, it creates namespaces as necessary and deletes
# them when they’re no longer needed. Typically, many namespaces will exist at any given time.

# 1 BUILT-IN

# The built-in namespace contains the names of all of Python’s built-in objects. These are available at all times
# when Python is running. You can list the objects in the built-in namespace with the following command:

dir(builtins)


# The Python interpreter creates the built-in namespace when it starts up. This namespace remains in existence
# until the interpreter terminates.

# 2 THE GLOBAL NAMESPACE

# The global namespace contains any names defined at the level of the main program. Python creates the global
# namespace when the main program body starts, and it remains in existence until the interpreter terminates.

# Strictly speaking, this may not be the only global namespace that exists. The interpreter also creates a global
# namespace for any module that your program loads with the import statement.

# 3 THE LOCAL AND ENCLOSING NAMESPACES

# As you learned in the previous tutorial on functions, the interpreter creates a new namespace whenever
# a function executes. That namespace is local to the function and remains in existence until the function terminates.

# Functions don’t exist independently from one another only at the level of the main program. You can also define
# one function inside another:

def f():
    print('Start f()')

    def g():
        print('Start g()')
        print('End g()')
        return

    g()

    print('End f()')
    return


f()

# When the main program calls f(), Python creates a new namespace for f(). Similarly, when f() calls g(), g() gets
# its own separate namespace. The namespace created for g() is the local namespace, and the namespace created for
# f() is the enclosing namespace.

# Each of these namespaces remains in existence until its respective function terminates. Python might not immediately
# reclaim the memory allocated for those namespaces when their functions terminate, but all references to the
# objects they contain cease to be valid.

# VARIABLE SCOPE

# The scope of a name is the region of a program in which that name has meaning. The interpreter determines this
# at runtime based on where the name definition occurs and where in the code the name is referenced.

# Example 1: Single Definition
# In the first example, x is defined in only one location. It’s outside both f() and g(), so it resides in
# the global scope:

x = 'global'


def f():
    def g():
        print(x)

    g()


f()

# The print() statement on line 81 can refer to only one possible x. It displays the x object defined in the global
# namespace, which is the string 'global'.

# Example 2: Double Definition
# In the next example, the definition of y appears in two places, one outside f() and one inside f() but outside g():

y = 'global'


def f():
    y = 'enclosing'

    def g():
        print(y)

    g()


f()

# According to the LEGB rule, the interpreter finds the value from the enclosing scope before looking in the global
# scope. So the print() statement displays 'enclosing' instead of 'global'.

# Example 3: Triple Definition
# Next is a situation in which x is defined here, there, and everywhere. One definition is outside f(), another
# one is inside f() but outside g(), and a third is inside g():

z = 'global'


def f():
    z = 'enclosing'

    def g():
        z = 'local'
        print(z)

    g()


f()

# Here, the LEGB rule dictates that g() sees its own locally defined value of x first. So the print() statement
# displays 'local'.

# PYTHON NAMESPACE DICTIONARIES

# A namespace is a dictionary in which the keys are the object names and the values are the objects themselves.
# In fact, for global and local namespaces, that’s precisely what they are! Python really does implement these
# namespaces as dictionaries.

# Note: The built-in namespace doesn’t behave like a dictionary. Python implements it as a module.

# Python provides built-in functions called globals() and locals() that allow you to access global and local
# namespace dictionaries.

# A SUBTLE DIFFERENCE BETTWEEN GLOBALS() AND LOCALS()

# There’s one small difference between globals() and locals() that’s useful to know about.
# globals() returns an ACTUAL REFERENCE to the dictionary that contains the global namespace. That means if you call
# globals(), save the return value, and subsequently define additional variables, then those new variables will show
# up in the dictionary that the saved return value points to:

g = globals()
print("The first reference to g: ", g)
print()

a = 'foo'
b = 29
print("The second reference to g: ", g)


# Here, g is a reference to the global namespace dictionary. After the assignment statements a = 'foo' and b = 29,
# they appear in the dictionary that g points to.

# locals(), on the other hand, returns a dictionary that is a CURRENT COPY of the local namespace, not a reference
# to it. Further additions to the local namespace won’t affect a previous return value from locals() until you call
# it again:

def f():
    s = 'foo'
    loc = locals()
    print("The first reference to s: ", loc)

    x = 20
    print("The second reference to s: ", loc)

    loc['s'] = 'bar'
    print("The third reference to s: ", loc)


f()

# In this example, loc points to the return value from locals(), which is a copy of the local namespace.
# The statement x = 20 adds x to the local namespace but not to the copy that loc points to.

# It’s a subtle difference, but it could cause you trouble if you don’t remember it.

# MODIFY VARIABLES OUT OF SCOPE

# Sometimes a function can modify its argument in the calling environment by making changes to the corresponding
# parameter, and sometimes it can’t:

# - An immutable argument can never be modified by a function.
# - A mutable argument can’t be redefined wholesale, but it can be modified in place.

# A similar situation exists when a function tries to modify a variable outside its local scope. A function can’t
# modify an immutable object outside its local scope at all:

k = 20


def f():
    k = 40
    return k


assert f() == 40
assert k == 20

# A function can modify an object of mutable type that’s outside its local scope if it modifies the object in place:

my_list = ['foo', 'bar', 'baz']


def f():
    my_list[1] = 'quux'


f()
assert my_list == ['foo', 'quux', 'baz']


# But if f() tries to reassign my_list entirely, then it will create a new local object and won’t modify the
# global my_list:

def f():
    my_list = ['qux', 'bar']
    return my_list


assert f() == ['qux', 'bar']
assert my_list == ['foo', 'quux', 'baz']

# THE GLOBAL DECLARATION

q = 20
assert q == 20


def f():
    global q
    q = 40
    print('q =', q)


f()

assert q == 40

# As you’ve already seen, globals() returns a reference to the global namespace dictionary. If you wanted to, instead
# of using a global statement, you could accomplish the same thing using globals():

j = 20
assert j == 20


def f():
    globals()['j'] = 40
    j = 40
    print('j =', j)


f()

assert j == 40


# If the name specified in the global declaration doesn’t exist in the global scope when the function starts, then
# a combination of the global statement and an assignment will create it:

# assert y == 20 -> error, because y hasn't yet been defined

def g():
    global y
    y = 20


# assert y == 20 -> error, because g hasn't been executed yet

g()
assert y == 20


# A name specified in a global declaration can’t appear in the function prior to the global statement:

# >>> def f():
# ...     print(x)
# ...     global x
# ...
# SyntaxError: name 'x' is used prior to global declaration

# THE NONLOCAL DECLARATION

# A similar situation exists with nested function definitions. The global declaration allows a function to access
# and modify an object in the global scope. What if an enclosed function needs to modify an object in the
# enclosing scope?

def f():
    x = 20

    def g():
        x = 40

    g()
    return x


assert f() == 20


# To modify x in the enclosing scope from inside g(), you need the analogous keyword nonlocal. Names specified after
# the nonlocal keyword refer to variables in the nearest enclosing scope:
def f():
    x = 20

    def g():
        nonlocal x
        x = 40

    g()
    return x


assert f() == 40

# Even though Python provides the global and nonlocal keywords, it’s not always advisable to use them.

# When a function modifies data outside the local scope, either with the global or nonlocal keyword or by directly
# modifying a mutable type in place, it’s a kind of side effect similar to when a function modifies one of its
# arguments. Widespread modification of global variables is generally considered unwise, not only in Python but also
# in other programming languages.
