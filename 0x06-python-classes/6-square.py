#!/usr/bin/python3
""" Class Square: defines a class with an instant variable size """


class Square:
    """ This defines the class square"""
    def __init__(self, size=0, position=(0, 0)):
        """
        initialization
        Args:
            size(int): the size of the square
            position(tuple): coordiantes of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Get the current size of the square """
        return self.__size

    @size.setter
    def size(self, size):
        """ Set the current size of the square """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        """retrieves the position(tuple of the square) """
        return self.__position

    @position.setter
    def position(self, value):
        """
        sets the position of the square
        Args:
            value(tuple): position of the square
        """
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[value[1]]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """area is a method that calcualtes the area of
        a sqaure given the size of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """ This prints the square"""
        if self.__size != 0:
            for i in range(self.__size):
               [print(" ", end="") for m in range(self.__position[0])]
               [print("#", end="") for n in range(self.__size)]
               print("")
        else:
            print()
