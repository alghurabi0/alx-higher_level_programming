#!/usr/bin/python3
""" checks if an object is an instance of a class. """


def is_kind_of_class(obj, a_class):
    """ check if obj is an instance of a_class.
        Returns: true of false.
    """

    return isinstance(obj, a_class)
