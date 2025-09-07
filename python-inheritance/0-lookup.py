#!/usr/bin/python3
"""
Module: 0-lookup
This module defines a function `lookup` that returns the list of available
attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj (any type): The object to inspect.

    Returns:
        list: List of attributes and methods of the object.
    """
    return dir(obj)
