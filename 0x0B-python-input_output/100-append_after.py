#!/usr/bin/python3
""" contains a module 'append_after' """


def append_after(filename="", search_string="", new_string=""):
    """ is a function that adds a new string """

    tmp = ""
    with open(filename) as nfile:
        for line in nfile:
            tmp = tmp + line
            if search_string in line:
                tmp += new_string

    with open(filename, 'w') as mfile:
        mfile.write(tmp)
