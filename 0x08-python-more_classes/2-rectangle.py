#!/usr/bin/python3
""" Rectangle class with two attributes. """


class Rectangle:
    """ Rectangle with width and height attributes. """
    def __init__(self, width=0, height=0):
        """ intialization of recangle instnce attributes.
        Args:
            self: self
            width: width
            height: height
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ return the private attribute of width. """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the private attribute of width.
        Args:
            value: value to set
        Returns: sets the width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ gets the private att of height. """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the private att of height.
        Args:
            value: value to set as height
        Returns: sets the value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Returns the area of the rectangle instance. """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns the perimeter of the rectange instance. """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
