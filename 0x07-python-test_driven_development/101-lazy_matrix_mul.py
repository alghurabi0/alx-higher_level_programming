#!/usr/bin/python3
""" Introduction matrix multiplication using NumPy. """


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        numpy.ndarray: The result of matrix multiplication.
    """
    np_m_a = np.array(m_a)
    np_m_b = np.array(m_b)

    result = np.matmul(np_m_a, np_m_b)

    return result
