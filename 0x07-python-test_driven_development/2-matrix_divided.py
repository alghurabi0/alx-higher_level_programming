#!/usr/bin/python3
""" Divides each element in a matrix by a a divisor. """


def matrix_divided(matrix, div):
    """ Divides each element in the matrix by div.

    Args:
        matrix: matrix to divide.
        div: divisor.

    Returns: New matrix.
    """

    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    length = len(matrix[0])
    new_matrix = []
    for arr in matrix:
        new_arr = []
        if len(arr) != length:
            raise TypeError('Each row of the matrix must have the same size')
        for num in arr:
            if not (isinstance(num, int) or isinstance(num, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
                num = round(num / div, 2)
                new_arr.append(num)
        new_matrix.append(new_arr)

    return new_matrix
