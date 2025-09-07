#!/usr/bin/python3
"""
Module 6-base_geometry
Defines a class BaseGeometry with an unimplemented area method.
"""


class BaseGeometry:
    """Class BaseGeometry with an unimplemented area method."""

    def area(self):
        """Raises an Exception indicating the method is not implemented."""
        raise Exception("area() is not implemented")
