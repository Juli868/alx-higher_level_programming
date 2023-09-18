#!/usr/bin/python3
"""create a new class."""


from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """Define a class that inherits Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the attributes.

        :param size: size of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Represent our object as a string."""
        return(f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}")
