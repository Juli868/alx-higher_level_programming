#!/usr/bin/python3
def no_c(my_string):
    cpy = ''
    for part in my_string:
        if part.lower() != 'c':
            cpy += part
    return (cpy)
