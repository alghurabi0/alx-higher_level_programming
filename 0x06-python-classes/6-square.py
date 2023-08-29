#!/usr/bin/python3
"""Difines a square class. """


class Square:
    """ Square class with optional size attribute. """
    def __init__(self, size=0, position=(0, 0)):
        """ Intialization of the sqaure class with size error handling.

        Args:
            size: an int, defines the size of the square instance.
            """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Method returns the position attribute. """
        return self.__position

    @position.setter
    def position(self, value):
        """ Method sets the position attribute for the square instance.

        Args:
            value: tuple to be set as a postion.
            """
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Returns: the area of the sqaure instance. """
        return self.__size * self.__size

    def my_print(self):
        """ Method that prints the square represented by # symbol. """
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for i in range(self.__size):
                    print("#", end="")
                print()
