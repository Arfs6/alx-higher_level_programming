#!/usr/bin/python3
"""
Write a function that prints x elements of a list.
"""


def safe_print_list(my_list=[], x=0):
    """
    print content of a list
    @my_list: content are in this list.
    @x: number of elements to print

    Return: number of elements printed
    """
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
        except IndexError:
            return i

    print("")
    return i + 1
