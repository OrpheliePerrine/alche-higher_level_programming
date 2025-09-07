#!/usr/bin/python3
"""Module defining MyList that inherits from list."""


class MyList(list):
    """A list subclass with a print_sorted method."""

    def print_sorted(self):
        """Prints the list in ascending order without modifying it."""
        print(sorted(self))
