#!/usr/bin/python3
""" MyInt class, rebel class ^^. """


class MyInt(int):
    """ MyInt class with special features. """
    def __new__(cls, value):
        """ Initialization of MyInt class."""
        return super().__new__(cls, value)

    def __eq__(self, other):
        """ overrides the == in int. """
        return not super().__eq__(other)

    def __ne__(self, other):
        """ overrides the != in int. """
        return not super().__ne__(other)
