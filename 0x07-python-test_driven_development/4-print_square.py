#!/usr/bin/python3
""" A module that prints a square using #, """


def print_square(size):
    """ a functio nthat prints a square

    Args:
        size: integer size of the square
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return print()

    for line in range(size):
        for block in range(size):
            print("#", end="")
        print()
