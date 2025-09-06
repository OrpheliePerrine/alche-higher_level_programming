#!/usr/bin/python3
"""
This module defines a Rectangle class that supports width and height,
computes area and perimeter, and can be printed using `#` characters.
"""


class Rectangle:
    """
    Represents a rectangle with width and height.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle.

        Args:
            width (int): Optional width (default is 0).
            height (int): Optional height (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieve the width of the rectangle.

        Returns:
            int: The current width.
        """
        return self.__width

    @width.setter
