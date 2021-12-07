# https://realpython.com/primer-on-python-decorators/#more-real-world-examples
import math


# ADDING INFORMATION ABOUT UNITS
# The following example is somewhat similar to the Registering Plugins example from earlier, in that it does not
# really change the behavior of the decorated function. Instead, it simply adds unit as a function attribute:

def set_unit(unit):
    """Register a unit on a function"""

    def decorator_set_unit(func):
        func.unit = unit
        return func

    return decorator_set_unit


# The following example calculates the volume of a cylinder based on its radius and height in centimeters:


@set_unit('cm^3')
def volume(radius, height):
    return math.pi * radius ** 2 * height


a = volume(3, 5)
a = float("{:.2f}".format(a))
assert a == 141.37
assert volume.unit == 'cm^3'
