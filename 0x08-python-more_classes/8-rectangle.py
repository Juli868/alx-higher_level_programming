#!/usr/bin/python3
"""Definition of a new class."""


class Rectangle:
    """description of the class."""

    number_of_instances = 0
    print_symbol = "#"

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
        type(self).number_of_instances += 1

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
                represent.append(str(self.print_symbol))
            if i != (self.__height - 1):
                represent.append("\n")
        return ("".join(represent))

    def __repr__(self):
        """Printable representaion."""
        repres = "Rectangle(" + str(self.__width)
        repres += ", " + str(self.__height) + ")"
        return repres

    def __del__(self):
        """Remove of an instance."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
        self.__width = None
        self.__height = None

    def bigger_or_equal(rect_1, rect_2):
        """Bigger_or_equal - determines the biggest among the rectangles.

        :param rect_1: first Rectangle
        :param rect_2: second Rectangle
        Return: rect_2 if it is the biggest else the rect_1
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (Rectangle.area(rect_1) < Rectangle.area(rect_2)):
            return rect_2
        return rect_1
