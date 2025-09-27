#!/usr/bin/python3
"""Module that contains the write_file function."""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the
    number of characters written.

    Args:
        filename (str): The path to the file to write to.
        text (str): The string to write.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
