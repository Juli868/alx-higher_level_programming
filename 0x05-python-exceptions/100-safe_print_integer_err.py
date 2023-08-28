#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    r_value = None
    try:
        print("{:d}".format(value))
        r_value = True
    except(TypeError):
        print("TypeError", file=sys.stderr)
        r_value = False
    finally:
        return(r_value)
