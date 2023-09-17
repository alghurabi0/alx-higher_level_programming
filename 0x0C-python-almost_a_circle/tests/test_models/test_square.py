#!/usr/bin/python3
""" Test Cases for the square class. """
import unittest
import io
import sys
from models.square import Square
import pycodestyle


class TestSquare(unittest.TestCase):

    def setUp(self):
        """
        result to stdout
        """
        sys.stdout = io.StringIO()

    def tearDown(self):
        """
        clean up after execution
        """
        sys.stdout = sys.__stdout__

    def test_pep8_model(self):
        """
        pep8 validation test module
        """
        p8 = pycodestyle.StyleGuide(quiet=True)
        p = p8.check_files(['models/square.py'])
        self.assertEqual(p.total_errors, 0, "fix pycodestyle")

    def test_pep8_test(self):
        """
        pep8 validation test
        """
        p8 = pycodestyle.StyleGuide(quiet=True)
        p = p8.check_files(['tests/test_models/test_square.py'])
        self.assertEqual(p.total_errors, 0, "fix pycodestyle")

    def test_docstrings(self):
        """ test cases for documentations. """
        self.assertIsNotNone(Square.__doc__)
        self.assertIs(hasattr(Square, "__init__"), True)
        self.assertIsNotNone(Square.__init__.__doc__)
        self.assertIs(hasattr(Square, "update"), True)
        self.assertIsNotNone(Square.update.__doc__)
        self.assertIs(hasattr(Square, "to_dictionary"), True)
        self.assertIsNotNone(Square.to_dictionary.__doc__)

    def test_square_creation(self):
        """ Test Cases for the square class. """
        s1 = Square(5, 0, 0, 1)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")

    def test_square_area(self):
        """ Test Cases for the square class. """
        s2 = Square(2, 2)
        self.assertEqual(s2.area(), 4)

    def test_square_display(self):
        """ Test Cases for the square class. """
        s3 = Square(3, 1, 3)

        captured_output = io.StringIO()
        sys.stdout = captured_output

        s3.display()

        sys.stdout = sys.__stdout__

        expected_output = "\n\n\n ###\n ###\n ###\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_square_with_custom_id(self):
        """ Test Cases for the square class. """
        s4 = Square(4, 2, 2, 42)
        self.assertEqual(str(s4), "[Square] (42) 2/2 - 4")

    def test_square_with_size_and_position(self):
        """ Test Cases for the square class. """
        s5 = Square(6, 3, 4, 2)
        self.assertEqual(str(s5), "[Square] (2) 3/4 - 6")

    def test_square_update_method(self):
        """ Test Cases for the square class. """
        s6 = Square(5)
        s6.update(10)
        self.assertEqual(str(s6), "[Square] (10) 0/0 - 5")

    def test_square_update_method_with_kwargs(self):
        """ Test Cases for the square class. """
        s7 = Square(3, 2, 2, 7)
        s7.update(id=8, size=4, x=1, y=1)
        self.assertEqual(str(s7), "[Square] (8) 1/1 - 4")

    def test_square_getter(self):
        """ Test Cases for the square class. """
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    def test_square_setter(self):
        """ Test Cases for the square class. """
        s2 = Square(5)
        s2.size = 10
        self.assertEqual(s2.size, 10)

    def test_square_setter_with_invalid_value(self):
        """ Test Cases for the square class. """
        s3 = Square(5)

        with self.assertRaises(ValueError) as context:
            s3.size = -5

        self.assertEqual(
            str(context.exception), "width must be > 0"
        )

        with self.assertRaises(ValueError) as context:
            s3.size = 0

        self.assertEqual(
            str(context.exception), "width must be > 0"
        )

        with self.assertRaises(TypeError) as context:
            s3.size = "9"

        self.assertEqual(
            str(context.exception), "width must be an integer"
        )

    def test_square_update_method(self):
        """ Test Cases for the square class. """
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")

        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")

        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")

        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")

        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")

        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")

        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

    def test_square_update_method_with_args_and_kwargs(self):
        """ Test Cases for the square class. """
        s2 = Square(5)
        s2.update(10, 2, x=3, y=4)
        self.assertEqual(str(s2), "[Square] (10) 3/4 - 2")

    def test_square_update_method_with_empty_args(self):
        """ Test Cases for the square class. """
        s3 = Square(3)
        s3.update(size=4, y=4, x=4, id=4)
        self.assertEqual(str(s3), "[Square] (4) 4/4 - 4")

    def test_square_update_method_invalid_size(self):
        """ Test Cases for the square class. """
        s5 = Square(3)
        with self.assertRaises(ValueError) as context:
            s5.update(size=0)

        self.assertEqual(
            str(context.exception), "width must be > 0"
        )

    def test_square_update_method_invalid_x(self):
        """ Test Cases for the square class. """
        s6 = Square(3)
        with self.assertRaises(ValueError) as context:
            s6.update(x=-1)

        self.assertEqual(
            str(context.exception), "x must be >= 0"
        )

    def test_square_update_method_invalid_y(self):
        """ Test Cases for the square class. """
        s7 = Square(3)
        with self.assertRaises(ValueError) as context:
            s7.update(y=-1)

        self.assertEqual(
            str(context.exception), "y must be >= 0"
        )

    def test_square_to_dictionary(self):
        """ Test Cases for the square class. """
        s1 = Square(10, 2, 1, 1)
        s1_dict = s1.to_dictionary()

        expected_dict = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(s1_dict, expected_dict)

    def test_square_from_dictionary(self):
        """ Test Cases for the square class. """
        s1 = Square(10, 2, 1)
        s1_dict = s1.to_dictionary()

        s2 = Square(1, 1)
        s2.update(**s1_dict)

        self.assertEqual(str(s1), str(s2))

    def test_square_to_dictionary_type(self):
        """ Test Cases for the square class. """
        s1 = Square(10, 2, 1)
        s1_dict = s1.to_dictionary()

        self.assertIsInstance(s1_dict, dict)

    def test_square_to_dictionary_multiple_objects(self):
        """ Test Cases for the square class. """
        s1 = Square(10, 2, 1, 1)
        s2 = Square(5, 0, 0, 2)
        s1_dict = s1.to_dictionary()
        s2_dict = s2.to_dictionary()

        expected_s1_dict = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        expected_s2_dict = {'id': 2, 'x': 0, 'size': 5, 'y': 0}

        self.assertDictEqual(s1_dict, expected_s1_dict)
        self.assertDictEqual(s2_dict, expected_s2_dict)


if __name__ == "__main__":
    unittest.main()
