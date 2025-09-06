#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute,
without type or value verification.
"""


class Square:
    """
    Represents a square with a private size attribute.

    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square (no verification performed).
        """
        self.__size = size
