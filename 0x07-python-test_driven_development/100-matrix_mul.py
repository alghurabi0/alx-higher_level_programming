#!/usr/bin/python3
""" A module that contain a function matrix_mul,
which is a function to multiply two matrices. """


def matrix_mul(m_a, m_b):
    """ A function that multiplies to matrices.

    Args:
        m_a: first matrix
        m_b: second matrix

    Returns: the product matrix
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for num in row:
            if not (isinstance(num, int) or isinstance(num, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for num in row:
            if not (isinstance(num, int) or isinstance(num, float)):
                raise TypeError("m_b should contain only integers or floats")

    row_len = len(m_a[0])
    for row in m_a:
        if len(row) != row_len:
            raise TypeError("each row of m_a must be of the same size")
    row_len = len(m_b[0])
    for row in m_b:
        if len(row) != row_len:
            raise TypeError("each row of m_b must be of the same size")

    cols_in_first = len(m_a[0])
    rows_in_second = len(m_b)
    if cols_in_first != rows_in_second:
        raise TypeError("m_a and m_b can't be multiplied")

    new_matrix = []
    for row in m_a:
        new_array = []
        for i in range(0, len(m_b[0])):
            j = 0
            new_val = []
            for col in row:
                new_val.append(col * m_b[j][i])
                j += 1
            x = 0
            for val in new_val:
                x += val
            new_array.append(x)
        new_matrix.append(new_array)

    return new_matrix
