#!/usr/bin/python3
"""Class determination."""


def is_same_class(obj, a_class):
    """Determine if is an instance."""
    if type(obj) is a_class:
        return True
    return False
