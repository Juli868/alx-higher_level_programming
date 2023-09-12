#!/usr/bin/python3
"""Deal with files."""


def write_file(filename="", text=""):
    """Write to a function."""
    with open(filename, 'w') as new_f:
        new_f.write(text)
    return len(text)
