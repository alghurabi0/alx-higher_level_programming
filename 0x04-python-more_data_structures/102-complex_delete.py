#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    my_list = []
    for key, val in a_dictionary.items():
        if val == value:
            my_list.append(key)
    for thing in my_list:
        del a_dictionary[thing]
    return a_dictionary
