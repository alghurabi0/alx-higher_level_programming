#!/usr/bin/python3
""" Unit testing for the max integer function. """

import unittest


max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Test cases for max integer.

    Returns: max integer in a list
    """

    def test_max_integer_basic(self):
        """ test max integer basic functionality. """
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_max_integer_reversed(self):
        """ Test a list of integers in reverse order. """
        result = max_integer([4, 3, 2, 1])
        self.assertEqual(result, 4)

    def test_max_integer_mixed(self):
        """ Test a list of mixed positive and negative integers. """
        result = max_integer([-1, 3, -4, 2])
        self.assertEqual(result, 3)

    def test_max_integer_empty_list(self):
        """ Test an empty list. """
        result = max_integer([])
        self.assertIsNone(result)

    def test_max_integer_single_element(self):
        """ Test a list with a single element. """
        result = max_integer([42])
        self.assertEqual(result, 42)


if __name__ == '__main__':
    unittest.main()
