#!/usr/bin/python3
"""defining a new class."""


class Square:
    """class elements."""

    def __init__(self, size=0):
        """Initialise the objects."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
