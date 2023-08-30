#!/usr/bin/python3
"""Create a new class."""


class Square:
    """Defining objects and instances."""

    def __init__(self, size=0):
        """Define the objects."""
        self.__size = size

    def size(self):
        """Searchiong for an object in class."""
        return(self.__size)

    def size(self, value):
        """Set the object."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area."""
        return (self.__size * self.__size)
