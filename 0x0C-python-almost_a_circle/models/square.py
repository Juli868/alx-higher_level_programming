#!/usr/bin/python3
"""create a new class."""


from rectangle import Rectangle
from base import Base


class Square(Rectangle):
    """Define a class that inherits Rectangle."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the attributes.
        :param size: size of the square.
        """
        super.__init__()
        self.__height = size
        self.__width = size
