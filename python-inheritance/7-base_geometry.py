#!/usr/bin/python3
"""
Module 7-base_geometry
Defines a class BaseGeometry with area() and integer_validator() methods.
"""


class BaseGeometry:
    """Class BaseGeometry with area() and integer_validator() methods."""

    def area(self):
        """Raises an Exception indicating the method is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Args:
            name (str): Name of the variable.
            value (int): Value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value <= 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
