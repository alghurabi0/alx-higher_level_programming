#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        best_key = next(iter(a_dictionary))
        for key in a_dictionary:
            if a_dictionary[key] > a_dictionary[best_key]:
                best_key = key
        return best_key
