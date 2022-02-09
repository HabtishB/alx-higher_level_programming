#!/usr/bin/python3
""" A module that contains a function "class_to_json(obj)" """
import json


def class_to_json(obj):
    """ A function that returns the dictionary description with simple
    data structures like (list, dictionary, strion, integer and boolean)
    for JSON serialization of an object """
    return obj.__dict__
