#!/usr/bin/python3
""" A square class that inherits from rectangle. """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A square class that inherits from rectangle. """
    def __init__(self, size):
        """ Initilization of the square class. """
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """ Format how square is printed. """
        return "[Square] {}/{}".format(self.__size, self.__size)
