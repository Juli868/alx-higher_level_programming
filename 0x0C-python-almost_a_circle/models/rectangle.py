#!/usr/bin/python3
"""Class creation."""
from models.base import Base


class Rectangle(Base):
    """Class definition."""

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

    @property
    def x(self):
        """Retreive x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x attibute."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieve y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y attribute."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialise of the attributes.

        :param widht: width of the rectangle.
        :param height: height of the rectangle.
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        if id is not None:
            self.id = id
        else:
            super().__init__()

    def area(self):
        """Calculate the area."""
        return (self.__width * self.__height)

    def display(self):
        """Print the rectangle."""
        for i in range(self.__height):
            for countuter in range(self.width):
                print('#', end='')
            print('')

    def __str__(self):
        """Represent object as a string."""
        first = (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - ")
        second = (f"{self.__width}/{self.__height}")
        return (first + second)
    def display(self):
        [print("") for i in range(0, self.__x)]
        for counter_1 in range(0, self.__height):
            [print(" ", end='')for i in range(0, self.__y)]
            [print("#", end='') for j in range(0, self.__width)]
            print("")
    def update(self, *args):
        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            elif i ==1:
                self.__width = args[i]
            elif i == 2:
                self.__height = args[i]
            elif i == 3:
                self.__x = args[i]
            elif i == 4:
                self.__y = args[i]
