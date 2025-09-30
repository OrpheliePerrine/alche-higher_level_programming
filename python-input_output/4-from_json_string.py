#!/usr/bin/python3
"""
This module provides a function that converts a JSON
string into a corresponding Python object.
"""

import json


def from_json_string(my_str):
    """
    Returns the Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string to be deserialized.

    Returns:
        object: The corresponding Python object (list, dict, int, str, etc.)
    """
    return json.loads(my_str)
