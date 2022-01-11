#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is not None:
        max_int = my_list[0]
        if my_list == []:
            return None
        else:
            for i in my_list:
                if i > max_int:
                    max_int = i
        return max_int
