#!/usr/bin/python3
"""create a class named square."""


class Square:
    """Defining objects and instances."""

    def __init__(self, size=0,position=(0,0)):
        """Define the objects."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Set a new object."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Assign a value to the attribute position."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(element, int) for element in value) or
                not all(element >= 0 for element in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print a square."""
        if (self.__size == 0):
            print("")
        else:
            [print("") for i in range(0,self.__position[1])]
            for counter_1 in range(0, self.__size):
                [print(" ", end='')for counter_2 in range(0, self.__position[0])]
                [print("#", end='') for j in range(0, self.__size)]
                print("")
