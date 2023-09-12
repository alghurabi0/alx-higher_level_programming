#!/usr/bin/python3
""" Save object to json file. """
import json


def save_to_json_file(my_obj, filename):
    """ Save object to json file. """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
