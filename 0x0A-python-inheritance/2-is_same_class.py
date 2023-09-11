#!/usr/bin/python3
""" checks if an object is an instance of a class. """


def is_same_class(obj, a_class):
    """ check if obj is an instance of a_class.
        Returns: true of false.
    """
    return type(obj) is a_class
