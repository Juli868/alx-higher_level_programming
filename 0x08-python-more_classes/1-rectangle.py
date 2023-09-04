#!/usr/bin/python3
"""Class definition."""


class Rectangle:
    """Illustrate elements of the  class."""

    def __init__(self, width=0, height=0):
        """Definition of the attributes."""
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Return the value of width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Define the width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("wigth must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return value of length."""
        return self.__height

    @height.setter
    def height(self, value):
        """Define the length attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("heigth must be >= 0")
        self.__height = value
