#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute,
using property getter and setter to control access and validation.
"""


class Square:
    """
    Represents a square with size validation through property.

    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square (default 0).
        """
        self.size = size  # Use setter for validation

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): The size value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
