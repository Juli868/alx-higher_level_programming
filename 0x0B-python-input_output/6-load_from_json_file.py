#!/usr/bin/python3
"""Deal with json files."""
import json


def load_from_json_file(filename):
    """Build from json file.

    @param filename: name of the json file.
    """
    with open(filename, 'r') as content:
        return (json.load(content))
