#!/usr/bin/python3
"""Pay with json."""
import json


def to_json_string(myobj):
    """Turn t json representation from string.

    @param myobj: string to work on
    Return: the json representation
    """
    return (json.dumps(myobj))
