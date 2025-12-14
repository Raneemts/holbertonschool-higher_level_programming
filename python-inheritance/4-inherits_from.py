#!/usr/bin/python3
"""Check if an object is instance of a subclass of a class"""


def inherits_from(obj, a_class):
    """Return True if obj inherits from a_class but is not excatly a_class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
