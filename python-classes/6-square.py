#!/usr/bin/python3
"""
This module defines a Square class with size and position attributes,
including validation, area calculation, and printing.
"""


class Square:
    """
    Represents a square with a size and position.

    Attributes:
        __size (int): The size of the square (private).
        __position (tuple): The position of the square (private).
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square (default 0).
            position (tuple): The position of the square (default (0, 0)).
        """
        self.size = size  # Will use setter validation
        self.position = position  # Will use setter validation

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The current size of the square.
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

    @property
    def position(self):
        """
        Retrieve the position of the square.

        Returns:
            tuple: The current position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square with validation.

        Args:
            value (tuple): The position value to set.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the character '#' to stdout,
        respecting the position attribute.

        Prints an empty line if size is 0.
        """
        if self.__size == 0:
            print()
            return

        # Print newlines for vertical position offset
        for _ in range(self.__position[1]):
            print()

        # Print each row of the square
        for _ in range(self.__size):
            # Print spaces for horizontal position offset
            print(" " * self.__position[0] + "#" * self.__size)
