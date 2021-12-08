#!/usr/bin/python3
""" Class Square: defines a class with an instant variable size """


class Square:
    def __init__(self, size=0):
        """ initialization """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = size
