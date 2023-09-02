#!/usr/bin/python3
""" Defines a locked class. """


class LockedClass:
    """ Private locked class. """

    def __setattr__(self, name, value):
        """ Initialization of the instance. """

        if name == 'first_name':
            self.__dict__[name] = value
        else:
            raise AttributeError(f"'LockedClass' object has no attribute '{name}'")
