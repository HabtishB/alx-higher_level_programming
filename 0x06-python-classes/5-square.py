#!/usr/bin/python3
""" Class Square: defines a class with an instant variable size """


class Square:

    def __init__(self, size=0):
        """ initialization """
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = size

    def area(self):
        area = self._size * self._size
        return area

    def my_print(self):
        if self._size != 0:
            for i in range(self._size):
                for j in range(self._size):
                    print("#", end="")
                print()
        else:
            print()
