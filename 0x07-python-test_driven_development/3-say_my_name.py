#!/usr/bin/python3
"""Define the name."""


def say_my_name(first_name, last_name=""):
    """Say_my_name - prints the fu name given to it.

    :param first_name: first name
    :param second_name: second name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
