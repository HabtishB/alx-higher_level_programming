#!/usr/bin/python3
""" This module contains a class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ Defines the class Rectangles, this class 
    inhertis from the Base module """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ This inistantiates the a rectangle object,
            the id is inherited from the Base module 
            Args:
                  width - width of the rectangle
                  height - height of the rectangle
                  x - the x-coordinate of the rectangle
                  y - the y- coordiante of the rectangle
        """

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter
        """
        if type(value) is not int:
            raise TypeError("height muust be an integer")
        elif value <= 0:
            raise ValueError("width muust be greate >= 0")
        else:
            self.__width = value
  
    @property
    def height(self):
        """ height getter
        """
        return self.__height

    
    @height.setter
    def height(self, value):
        """ height setter
        """
        if type(value) is not int:
            raise TypeError("height muust be an integer")
        elif value <= 0:
            raise ValueError("height muust be greater >= 0")
        else:
            self.__width = value

    @property
    def x(self):
        """ x getter
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ width setter
        """
        if value < 0:
            raise ValueError("x must be greater > 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ x -getter
        """
        return self.__y

    @y.setter
    def y(self, value):
        """ width setter
        """
        if value < 0:
            raise ValueError("y must be greater > 0")
        else:
            self.__y = value

    def area(self):
        """ Calculates the area of the rectangle(width, height)
        """
        return self.__width * self.__height

    def display(self):
        """ displays the rectangle using "#"
        """
        tmp = self.__width
        if self.y > 0:
            print("\n" * (self.y - 1))
        for self.__width in range(self.__height):
            print(" " * self.x + "#" * tmp)

    def __str__(self):
        """ define the rectangle in strings """    
        return "[Rectangle] ({0}) {3}/{4} - {1}/{2}".format(self.id, self.__width, self.__height, self.__x, self.__y)

    def update(self, *args, **kwargs):
        """ This updates the Rectangle attributes
        """
        attributes = ["id", "width", "height", "x", "y"]
        if args is not None and len(args) is not 0:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
                
        for key, value in kwargs.items():
            setattr(self, key, value)
