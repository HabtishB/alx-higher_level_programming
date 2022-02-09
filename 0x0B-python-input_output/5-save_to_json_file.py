#!/usr/bin/python3
""" A module that contains 'save_to_json_file' function """
import json


def save_to_json_file(my_obj, filename):
    """ A function that writes an Object to a text file, 
    using a JSON representation """

    with open(filename, encoding="UTF-8", mode="w") as json_file:
        json_file.write(json.dumps(my_obj))
