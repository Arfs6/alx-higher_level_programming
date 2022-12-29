#!/usr/bin/python3
"""Using map() on a list"""


def multiply_list_map(my_list=[], number=0):
    """multiply all elements in the list with the number passed

    Parameter:
    - my_list: list containing objects to be multiplied
    - number: number to multiply with

    Returns:
    - new list with all item multiplied
    """
    mul_list = []
    if not my_list:
        return mul_list
    elif not isinstance(my_list, list):
        return None

    mul_list = map(lambda x, y: x * y, my_list, [number for i in my_list])
    return list(mul_list)
