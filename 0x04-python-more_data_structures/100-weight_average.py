#!/usr/bin/python3
def weight_average(my_list=[]):
    new_list = list(map(lambda item: (item[0] * item[1], item[1]), my_list))
    score = 0
    weight = 0
    for num in new_list:
        score += num[0]
        weight += num[1]
    return score / weight
