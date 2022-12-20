#!/usr/bin/python3
"""A square class with a private instance attribute"""


class Square:
    """A representaion of a square"""

    def __init__(self, size):
        """initialize a new square instance"""
        self.size = size

        @property
        def size(self):
            return self.__size

    @size.setter(self, size):
        self.__size = size
