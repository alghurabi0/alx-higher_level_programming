#!/usr/bin/python3
""" A student class. """


class Student:
    """ A student class. """
    def __init__(self, first_name, last_name, age):
        """ Initilization of the student class. """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns a dict with cls attrs. """
        if isinstance(attrs, list):
            if all(isinstance(attr, str) for attr in attrs):
                return {attr: getattr(self, attr, None) for
                        attr in attrs if getattr(self, attr, None) is not None}

        return self.__dict__

    def reload_from_json(self, json):
        """ Override exsting attributes. """
        for key, value in json.items():
            setattr(self, key, value)
