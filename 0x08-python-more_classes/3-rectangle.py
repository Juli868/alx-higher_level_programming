#!/usr/bin/python3
"""Definition of a new class."""


class Rectangle:
    """description of the class."""

    @property
    def width(self):
        """Default set width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Default setting height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        """Initialise of class attributes."""
        self.__height = height
        self.__width = width

    def area(self):
        """Calculate the area."""
        return self.__height * self.__width

    def perimeter(self):
        """Calculate perimeter."""
        if (self.__width == 0 or self.__height == 0):
            return 0
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """Readable representation."""
        represent = []
        if (self.__width == 0):
            return ("")
        for i in range(self.__height):
            for k in range(self.__width):
                represent.append("#")
            represent.append('\n')
        return ("".join(represent))
