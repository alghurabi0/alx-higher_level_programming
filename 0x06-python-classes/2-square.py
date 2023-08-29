#!/usr/bin/python3
"""Difines a square class. """


class Square:
    """ Square class with optional size attribute. """
    def __init__(self, size=0):
        """ Intialization of the sqaure class with size error handling.

        Args:
            size: an int, defines the size of the square instance.
            """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
