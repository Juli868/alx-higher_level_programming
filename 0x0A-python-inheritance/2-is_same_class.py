#!/usr/bin/python3
"""Class determination."""


def is_same_class(obj, a_class):
    """Determine if is an instance."""
    if isinstance(obj, a_class):
        return True
    return False
