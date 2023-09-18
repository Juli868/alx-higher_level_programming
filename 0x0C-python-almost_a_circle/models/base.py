#!/usr/bin/python3
"""Define a class."""


class Base:
    """Class base definition."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialise all atributes."""
        if(id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def load_from_file(cls):
        return (self.__nb_objects)
