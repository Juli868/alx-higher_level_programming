#!/usr/bin/python3
"""Deal with files."""


def read_file(filename=""):
    """Read content from a file."""
    with open(filename, 'r', encoding='UTF-8') as new:
        print(new.read(), end='')
