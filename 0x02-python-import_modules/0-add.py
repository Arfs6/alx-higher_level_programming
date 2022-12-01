#!/usr/bin/python3
from add_0 import add


def test():
    """ test if the add function is working """
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b))


# execute only if file is not imported
if __name__ == "__main__":
    test()
