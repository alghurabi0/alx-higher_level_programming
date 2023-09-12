#!/usr/bin/python3
""" Gets class attrs and instance attrs in a dict. """


def class_to_json(obj):
    """ Gets class attrs and instance attrs. """
    inst_attr = obj.__dict__

    return inst_attr
