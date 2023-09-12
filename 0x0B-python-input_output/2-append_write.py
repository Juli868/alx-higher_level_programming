#!/usr/bin/python3
"""Deal with files."""


def append_write(filename="", text=""):
    """Append to a file.

    @param filename: name of the file.
    @param text: text to appent to a file.
    """
    with open(filename, 'a') as new_f:
        new_f.write(text)
    return len(text)
