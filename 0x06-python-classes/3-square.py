#!/usr/bin/python3
"""defining a new class."""


class Square:
    """define the objects."""

    def __init__(self, size=0):
        """Assign values to the objets."""
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
            """Calculate the area using object."""
            return self.__size * self.__size
