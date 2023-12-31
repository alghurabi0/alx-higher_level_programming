#!/usr/bin/python3
""" Rectangle class that inherits from geometry. """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class that inherits from GeoMetry. """
    def __init__(self, width, height):
        """ Intialization of the rectangle class. """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
