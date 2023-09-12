#!/usr/bin/python3
"""Deal with files."""


def read_file(filename=""):
    """Read content from a file."""
    with open(filename, 'r') as new:
        content = new.read
    print(content)
