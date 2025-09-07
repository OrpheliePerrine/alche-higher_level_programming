#!/usr/bin/python3
"""
Module 4-inherits_from
Defines a function that checks if an object is an instance of a class
that inherits (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherits from
    a_class (excluding exact instances of a_class), otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        bool: True if obj is an instance of a subclass of a_class, else False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
