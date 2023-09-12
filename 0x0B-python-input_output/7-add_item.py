#!/usr/bin/python3
""" Adds arguments to python list. """
import sys
import json


if __name__ == "__main__":
    pyToJson = __import__('5-save_to_json_file').save_to_json_file
    jsonToPy = __import__('6-load_from_json_file').load_from_json_file

    filename = "add_item.json"

    try:
        my_list = jsonToPy(filename)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        my_list = []

    for arg in sys.argv[1:]:
        my_list.append(arg)

    pyToJson(my_list, filename)
