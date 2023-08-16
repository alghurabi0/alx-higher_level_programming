#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for el in row:
            new_row.append(el * el)
        new_matrix.append(new_row)
    return new_matrix
