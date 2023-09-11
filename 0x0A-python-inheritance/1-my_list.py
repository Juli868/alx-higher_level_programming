#!/usr/bin/python3
"""Define class MyList."""


class MyList(list):
    """Instance of list."""

    def print_sorted(self):
        """Sort a list."""
        new_list = self[:]
        for i in range(len(new_list)):
            if not isinstance(new_list[i], int):
                raise TypeError("Element must be int")
        print(sorted(new_list))
