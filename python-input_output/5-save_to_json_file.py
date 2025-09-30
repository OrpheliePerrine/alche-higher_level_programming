#!/usr/bin/python3
"""
This module provides a function that writes an object to
a text file using its JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using JSON representation.

    Args:
        my_obj (any): The object to be serialized and written.
        filename (str): The name of the file to write to.

    Returns:
        None
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
