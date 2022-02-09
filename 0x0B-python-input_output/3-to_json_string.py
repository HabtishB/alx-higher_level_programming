#!/usr/bin/python3
"""A module that contains '3-to_json_string.py' function """
import json


def to_json_string(my_obj):
    """ A function that returns the JSON representation of an object
    (string) """
    return json.dumps(my_obj)
