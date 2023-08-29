#!/usr/bin/python3
"""Defines a sqaure class with private size att"""


class Square:
    """Square class with size attribute"""
    def __init__(self, size):
        """Intialize a new square instance

        Args:
            size: int that defines the square size.
            """

        self.__size = size
