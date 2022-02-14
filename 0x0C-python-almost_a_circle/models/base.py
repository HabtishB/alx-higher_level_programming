#!/usr/bin/python3
""" A module that contains base class """

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """ This initializes id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id =Base.__nb_objects

        
