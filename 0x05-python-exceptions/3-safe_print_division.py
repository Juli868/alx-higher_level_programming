#!/usr/bin/python3:
def safe_print_division(a, b):
    c = None
    try:
        c = a / b
    except (UnboundLocalError,ZeroDivisionError):
        return None
    finally:
        return c
