#!/usr/bin/python3
""" Simple add integer module.
parameters only integers and float accepted."""


def add_integer(a, b=98):
    """ A simple add integer function.

    Args:
        a: integer
        b: integer

    Returns: the sum of integers.
    """

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError('a must be an integer')
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
