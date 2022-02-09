#!/usr/bin/python3
""" contains the class 'Student' """


class Student:
    """ This class defines a student """
    def __init__(self, first_name, last_name, age):
        """ instantiation of the attributes """

        self.first_name = ""
        self.last_name = ""
        self.age = 0
        if isinstance(first_name, str):
            self.first_name = first_name
        if isinstance(last_name, str):
            self.last_name = last_name
        if type(age) == int:
            self.age = age

    def to_json(self):
        """ this function retrieves a dictionary representation of a 'Student'
        instance) """

        return self.__dict__
