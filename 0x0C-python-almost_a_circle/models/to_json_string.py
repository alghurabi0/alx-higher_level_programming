#!/usr/bin/python3
""" Serialize a string object to JSON format. """
import json


def to_json_string(my_obj):
    """ Serialize a string object to JSON format. """
    return json.dumps(my_obj)
