#!/usr/bin/python3
""" An empty 5-base_geometry.py class. """


class BaseGeometry:
    """ an empty BaseGeometry class. """
    def area(self):
        """ raises an exception with message. """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates the value parameter. """
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
