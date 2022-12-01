#!/usr/bin/python3
from sys import argv


def run():
    """print arguments the file was called with"""
    argc = len(argv)

    if argc == 1:
        print("0 arguments.")
        return

    idx = 0
    for arg in argv:
        if idx == 0:
            idx += 1
            continue
        print("{:d}: {:s}".format(idx, arg))
        idx += 1


if __name__ == "__main__":
    run()
