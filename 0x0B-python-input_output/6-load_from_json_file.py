#!/usr/bin/python3
""" A module that contains a function "load_from_json_file" """
import json


def load_from_json_file(filename):
    """ A function that creates an Object from a "JSON file"
    """
    with open(filename, encoding='UTF-8', mode='r') as f:
        return json.load(f)
