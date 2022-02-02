#!/usr/bin/python3


def magic_string(magic_list=[0]):
    magic_list[0] = magic_list[0] + 1
    return (", ".join("BestSchool" for magic_list in range(magic_list[0])))
