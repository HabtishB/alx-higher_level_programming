#!/usr/bin/python3
""" A module that contains only the class Rectangle """


class Rectangle:
    """ A class for rectangles """
    def __init__(self, width=0, height=0):
        """ initialization"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter for width """
        return self.width

    @property
    def height(self):
        """ getter for height """
        return self.height

    @width.setter
    def width(self, value):
        """ sets the width of the rectangle to value """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.width = value

    @height.setter
    def height(self, value):
        """ sets the height of the rectangle to value """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.height = value
