#!/usr/bin/python3
"""
create an empty class to represent a geometry
"""


class BaseGeometry:
    """a class that represents a geometry"""

    def area(self):
        """Raises an exception"""
        raise(Exception("area() is not implemented"))

    def integer_validator(self, name, value):
        """Check if the right integer was passed
        Parameter:
        - name: name of integer. Use for printing error
        - value: integer to inspect.
        Raises:
        - TypeError: value is not an integer
        - ValueError: value is less than zero
        """
        if not isinstance(value, int):
            raise(TypeError(f"{name} must be an integer"))
        elif value <= 0:
            raise(ValueError(f"{name} must be greater than 0"))


class Rectangle(BaseGeometry):
    """A class that represents a rectangle"""

    def __init__(self, width, height):
        """initialize the attributes of the rectangle
        Parameter:
        - height: height of rectangle. An integer greater than zero
        - width: width of rectangle. An integer greater than zero
        """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width
