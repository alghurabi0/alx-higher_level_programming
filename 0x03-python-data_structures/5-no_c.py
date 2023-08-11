#!/usr/bin/python3
def no_c(my_string):
    my_list = [char for char in my_string]
    for el in my_list:
        if el == 'c' or el == 'C':
            my_list.remove(el)
    new_str = ''.join(my_list)
    return new_str
