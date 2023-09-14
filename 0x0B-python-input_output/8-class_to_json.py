#!/usr/bin/python3
"""Deal with json."""


def class_to_json(obj):
    """Trasnform to json object.

    @param obj: object to deal with.
    """
    return (obj.__dict__)
