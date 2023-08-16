#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    new_list = list(map(lambda item: (item[0] * item[1], item[1]), my_list))
    score = 0
    weight = 0
    for num in new_list:
        score += num[0]
        weight += num[1]
    return score / weight
