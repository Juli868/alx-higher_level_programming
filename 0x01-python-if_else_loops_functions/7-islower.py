#!/usr/bin/python3
def islower(c):
    for character in range(97, 123):
        if (type(c) is str):
            if (c == chr(character) and type(c) is str):
                return True
            else:
                return False
        else:
            return -1
