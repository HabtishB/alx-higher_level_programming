#!/usr/bin/python3
""" A module that contains a function '0-read_file'"""


def read_file(filename=""):
    """ A function that reads a text file in "UTF-8" and
    prints it to a std out
    Arguments:
        @filename - is the name of the file
    """
    with open(filename, encoding="UTF-8") as filetoread:
        filetowrite = filetoread.read()
        print(filetowrite, end="")
