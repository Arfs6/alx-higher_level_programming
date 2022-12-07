#!/usr/bin/python3
"""
Write a function that returns a key with the biggest integer value.
"""


def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    _max = None
    for key in a_dictionary:
        if _max is None:
            _max = a_dictionary[key]
            continue
        if _max < a_dictionary[key]:
         _max = a_dictionary[key]

    return _max
