#!/usr/bin/python3
""" A module that contains a function '2-append_write.py' """


def append_write(filename="", text=""):
    """ A function that appends a string at the end of the text (UTF-8)
    and returns the number of characters added """
    with open(filename, encoding='UTF-8', mode='a') as file_appended:
        return file_appended.write(str(text))
