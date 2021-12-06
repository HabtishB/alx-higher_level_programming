#!/bin/bash
#0-safe_print_list.py
def safe_print_list(my_list=[], x=0):
    num = 0

    try:
        while num < x:
              print(my_list[num], end = " ")
	      num += 1

    except IndexError:
        pass

    print("\n")
    return num

        
    
