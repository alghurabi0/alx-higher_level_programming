#!/usr/bin/python3
"""Difines a square class. """


class Square:
    """ Square class with optional size attribute. """
    def __init__(self, size=0):
        """ Intialization of the sqaure class with size error handling.

        Args:
            size: an int, defines the size of the square instance.
            """
        self.size = size

    @property
    def size(self):
        """ Public class method to get the size of the square instance. """
        return self.__size

    @size.setter
    def size(self, value):
        """ Class method that sets the size attibute of the square instance.

        Args:
            value: the size value to be set.
            """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Returns: the area of the sqaure instance. """
        return self.__size * self.__size

    def __eq__(self, other):
        """ Checks for the equal case.


        Args:
            other: other instance of square.
            """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """ Checks for the not equal case.

        Args:
            other: checks for other instance of square.
            """
        if isinstance(other, Square):
            return self.area() != other.area()
        return True

    def __gt__(self, other):
        """ Checks for the greater than case.

        Args:
            other: other instance of square.
            """
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """ Checks for the lower equal case.

        Args:
            other: other instance of square.
            """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False

    def __lt__(self, other):
        """ Checks for the lower thatn case.

        Args:
            other: other instance of squre.
            """
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """ Checks for the lower equal case.

        Args:
            other: other instance of squar.
            """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False
