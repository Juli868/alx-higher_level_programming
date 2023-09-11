#!/usr/bin/python3
"""Detrmine the usage."""


def is_kind_of_class(obj, a_class):
    """Determine if it is an instance or not."""
    if isinstance(obj, a_class):
        return True
    return False
