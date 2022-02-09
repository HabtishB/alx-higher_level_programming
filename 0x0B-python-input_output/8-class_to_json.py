#!/usr/bin/python3
""" A module that contains a function "class_to_json(obj)" """
import json


def class_to_json(obj):
    """ A function that returns the dictionary description with simple
    data structures like (list, dictionary, strion, integer and boolean)
    for JSON serialization of an object 
    """
    data = {}
    for attr in obj.__dict__:
        data[attr] = obj.__dict__[attr]
    return data
