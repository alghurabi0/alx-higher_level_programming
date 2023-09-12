#!/usr/bin/python3
""" A student class. """


class Student:
    """ A student class. """
    def __init__(self, first_name, last_name, age):
        """ Initilization of the student class. """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Returns a dict with cls attrs. """
        return self.__dict__
