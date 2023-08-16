#!/usr/in/python3
def multiply_by_2(a_dictionary):
    my_dic = dict(a_dictionary)
    for key in my_dic:
        my_dic[key] = my_dic[key] * 2
    return my_dic
