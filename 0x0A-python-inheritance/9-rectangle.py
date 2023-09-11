#!/usr/bin/python3
""" Rectangle class that inherits from geometry. """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class that inherits from GeoMetry. """
    def __init__(self, width, height):
        """ Intialization of the rectangle class. """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)

    def area(self):
        """ Returns the area of the rectagnle. """
        return self.__width * self.__height

    def __str__(self):
        """ format how rectangle class is printed to std output. """
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
