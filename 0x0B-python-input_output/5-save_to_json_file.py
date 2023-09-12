#!/usr/bin/python3
"""Deal with json."""
import json


def save_to_json_file(myobj, filename):
    """Save to a json file.

    @param myobj:  the file to add to the file.
    @param filename: name of the file.
    """
    new_str = json.dumps(myobj)
    with open(filename, 'w') as new_file:
        new_file.write(new_str)
