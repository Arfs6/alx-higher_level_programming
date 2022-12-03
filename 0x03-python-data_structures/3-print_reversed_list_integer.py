#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """
    print_reversed_list_integer: prints integers in a list in reverse order
    @my_list: list to print
    """
    my_list.reverse()

    for num in my_list:
        print("{:d}".format(num))

    my_list.reverse()  # setting list back to it's original state
