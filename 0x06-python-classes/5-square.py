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
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Returns: the area of the sqaure instance. """
        return self.__size * self.__size

    def my_print(self):
        """ Method that prints the square represented by # symbol. """
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                for i in range(self.__size):
                    print("#", end="")
                print()
