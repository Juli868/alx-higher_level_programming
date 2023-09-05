#!/usr/bin/python3
"""Define a function to find a sum of two numbers."""


def add_integer(a, b=98):
    """
    add_integer: adds tw numbers.

    :param a: first number.
    :param b: secnd number.
    :return: the sum.
    """
    if not ((type(a) is int) or (type(a) is float)):
        raise TypeError("a must be an integer")
    elif not (type(b) is int or type(b) is float):
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
