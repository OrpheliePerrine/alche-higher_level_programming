#!/usr/bin/python3
"""Square class inheriting from Rectangle with custom __str__."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class with size, area, and string representation."""

    def __init__(self, size):
        """Initialize Square with validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return string representation of the square."""
        return "[Square] {}/{}".format(
            self._Rectangle__width, self._Rectangle__height
        )
