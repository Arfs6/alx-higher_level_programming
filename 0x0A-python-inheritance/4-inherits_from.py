#!/usr/bin/python3
"""
checks if an object is a subclass of a class
"""


def inherits_from(obj, a_class):
    """check if obj is sub classof a_class"""
    return issubclass(type(obj), a_class)
