# Some commonly used decorators that are even built-ins in Python are @classmethod, @staticmethod, and @property.
# The @classmethod and @staticmethod decorators are used to define methods inside a class namespace that are NOT
# connected to a particular instance of that class. The @property decorator is used to customize getters and setters
# for class attributes.
# Examples using these decorators.

# The following definition of a Circle class uses the @classmethod, @staticmethod, and @property decorators:

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Get value of radius"""

        # .radius is a MUTABLE PROPERTY: it can be set to a different value. However, by defining a setter method,
        # we can do some error testing to make sure it’s not set to a nonsensical negative number.
        # PROPERTIES ARE ACCESSED AS ATTRIBUTES WITHOUT PARENTHESES

        return self._radius

    @radius.setter
    def radius(self, value):
        """Set radius, raise error if negative"""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    @property
    def area(self):
        """Calculate area inside circle"""

        # .area is an IMMUTABLE PROPERTY: properties without .setter() methods can’t be changed. Even though it is
        # defined as a method, it can be retrieved AS AN ATTRIBUTE without parentheses.

        return self.pi() * self.radius ** 2

    def cylinder_volume(self, height):  # it is a regular method
        """Calculate volume of cylinder with circle as base"""
        return self.area * height

    @classmethod
    def unit_circle(cls):
        """Factory method creating a circle with radius 1"""

        # .unit_circle() is a class method. It’s not bound to one particular instance of Circle. Class methods
        # are often used as factory methods that can create specific instances of the class.

        return cls(1)

    @staticmethod
    def pi():
        """Value of π, could use math.pi instead though"""

        # .pi() is a static method. It’s NOT really DEPENDENT on the Circle class, except that it is part of its
        # namespace. Static methods CAN BE CALLED ON EITHER AN INSTANCE OR THE CLASS.

        return 3.1415926535


c = Circle(5)
assert c.radius == 5
assert c.area == 78.5398163375

c.radius = 7
assert c.radius == 7

# c.area = 15 --> AttributeError: can't set attribute --> because area property is without .setter method

assert c.cylinder_volume(height=4) == 615.752160086

# c.radius = -1 --> ValueError: Radius must be positive

c = Circle.unit_circle()
assert c.radius == 1

assert c.pi() == 3.1415926535

assert Circle.pi() == 3.1415926535
