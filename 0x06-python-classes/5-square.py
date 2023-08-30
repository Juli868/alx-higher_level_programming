#!/usr/bin/python3
"""create a class named square."""


class Square:
    """Defining objects and instances."""

    def __init__(self, size=0):
        """Define the objects."""
        self.__size = size

    @property
    def size(self):
        """Searchiong for an object in class."""
        return (self.__size)

    @size.setter
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

    def my_print(self):
        """Print a square."""
        if (self.__size == 0):
            print("")
        else:
            for counter_1 in range(0, self.__size):
                for counter_2 in range(0, self.__size):
                    print("#", end='')
                print("")
