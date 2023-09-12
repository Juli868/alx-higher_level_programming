#!/usr/bin/python3
"""Dealing with json."""


import json

def from_json_string(my_str):
    """Turn into  python string from json string.

    @param my_str: string to work on.
    """ 
    return (json.loads(my_str))
