#!/usr/bin/python3
""" Convert json tring to python object. """
import json


def from_json_string(my_str):
    """ Convert json string to python object. """
    return json.loads(my_str)
