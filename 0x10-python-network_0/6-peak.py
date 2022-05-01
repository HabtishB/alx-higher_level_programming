#!/usr/bin/python3

"""
find peak task
"""

def find_peak(list_of_integers):
    """ finds a peak in  unsorted integers """
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
