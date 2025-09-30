#!/usr/bin/python3
"""
This module provides a function that returns the dictionary
description of a class instance, containing only simple
serializable attributes (list, dict, str, int, bool).
"""


def class_to_json(obj):
    """
    Returns the dictionary representation of a class instance.

    Args:
        obj (object): The instance of a class.

    Returns:
        dict: A dictionary containing all attributes of obj
              suitable for JSON serialization.
    """
    return obj.__dict__.copy()
