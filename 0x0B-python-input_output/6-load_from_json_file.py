#!/usr/bin/python3
""" Creates object from json file. """
import json


def load_from_json_file(filename):
    """ Creates object from json file. """
    with open(filename) as file:
        return json.load(file)
