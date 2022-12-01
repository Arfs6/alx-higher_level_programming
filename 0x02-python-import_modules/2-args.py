#!/usr/bin/python3
import argparse as ap


def run():
    """print arguments the file was called with"""
    parser = ap.ArgumentParser(
            description="pass me arguments and i will print it for you :)"
            )
    parser.add_argument("args", nargs="*")
    _args = parser.parse_args()
    argv = _args.args
    argc = len(argv)

    if argc == 0:
        print("0 arguments.")
        return

    idx = 1
    for arg in argv:
        print("{}: {}".format(idx, arg))
        idx += 1


if __name__ == "__main__":
    run()
