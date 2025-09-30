#!/usr/bin/python3
"""
This module defines a Student class with public attributes
and methods to serialize and deserialize its instances.
"""


class Student:
    """
    Represents a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student instance.

        If attrs is a list of strings, only attributes with names
        in this list will be included. Otherwise, all attributes
        are included.

        Args:
            attrs (list, optional): List of attribute names to include.

        Returns:
            dict: Dictionary representation of the instance.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {
                key: value
                for key, value in self.__dict__.items()
                if key in attrs
            }
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance based on a dictionary.

        Args:
            json (dict): A dictionary containing attribute names as keys
                         and values to set.
        """
        for key, value in json.items():
            setattr(self, key, value)
