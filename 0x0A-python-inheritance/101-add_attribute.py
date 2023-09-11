#!/usr/bin/python3
""" Adds new attribute to an object if possible. """


def add_attribute(obj, attr_name, attr_value):
    """ The function that adds the attribute to the object. """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, attr_name, attr_value)
