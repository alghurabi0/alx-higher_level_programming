#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda array: list(map(lambda num: (num * num), array)), matrix))
