#!/usr/bin/python3
"""
Write a function that prints x elements of a list.
"""

def safe_print_list(my_list=[], x=0):
    """
    print content of a list
    @my_list: content are in this list.
    @x: number of elements to print
    """
    for i in range(x):
        try:
            print(f"{my_list[i]}");
        except IndexError:
            return i

    return i + 1
