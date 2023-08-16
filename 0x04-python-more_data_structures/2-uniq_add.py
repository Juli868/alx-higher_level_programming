#!/usr/bin/python3
def uniq_add(my_list=[]):
    added = 0
    numbers = set(my_list)
    for counter in numbers:
        added += counter
    return (added)
