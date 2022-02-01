#!/usr/bin/python3
""" A module that contains only the class Rectangle """


class Rectangle:
    """ A class for rectangles """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initialization"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ getter for width """
        return self.__width

    @property
    def height(self):
        """ getter for height """
        return self.__height

    @width.setter
    def width(self, value):
        """ sets the width of the rectangle to value """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ sets the height of the rectangle to value """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ compares the area of two rectangles and
            returns the bigger rectangle
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)

    def area(self):
        """ calculates the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ calculates the perimeter of the rectangle """
        if (self.__width == 0 or self.__height == 0):
            return 0
        return (2 * self.__width + 2 * self.__height)

    def __str__(self):
        """ returns a '#' respresentation of the rectangle"""
        if self.__width != 0 and self.__height != 0:
            hash_rep = ""
            hash_rep += "\n".join(str(self.print_symbol) * self.__width
                                  for i in range(self.__height))
            return hash_rep
        else:
            return ""

    def __del__(self):
        """prints a message when an instance of a rectangle is deleted """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
