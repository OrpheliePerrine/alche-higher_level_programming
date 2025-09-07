#!/usr/bin/python3
"""
Module 3-is_kind_of_class
Defines a function that checks if an object is an instance of a class or
an instance of a class that inherited from the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or an instance of a subclass
    of a_class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        bool: True if obj is instance of a_class or subclass, else False.
    """
    return isinstance(obj, a_class)
