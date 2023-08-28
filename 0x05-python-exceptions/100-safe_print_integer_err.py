#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    r_value = None
    try:
        print("{:d}".format(value))
        r_value = True
    except(TypeError):
        print("Exception: {}".format(sys.exc_info[1]), file=sys.stderr)
        r_value = False
    finally:
        return(r_value)
