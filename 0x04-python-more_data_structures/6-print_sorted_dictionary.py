#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dic = sorted(a_dictionary)
    for item in sorted_dic:
        print('{}: {}'.format(item, a_dictionary[item]))
