#!/usr/bin/python3
"""Subclass determination."""


def inherits_from(obj, a_class):
    """Define if there is a subclass provided."""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
