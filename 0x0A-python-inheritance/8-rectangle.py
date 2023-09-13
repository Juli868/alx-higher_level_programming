#!/usr/bin/python3
"""Define a class."""


class BaseGeometry:
    """class elements."""

    def area(self):
        """Area calculation."""
        raise Exception("area() is not implemeted")

    def integer_validator(self, name, value):
        """Set value to the attributes."""
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Definitin of a new class."""

    def __init__(self, width, height):
        """Initialize attributes."""
        Rectangle.integer_validator
