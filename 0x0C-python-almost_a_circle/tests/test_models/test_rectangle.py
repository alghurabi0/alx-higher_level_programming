#!/usr/bin/python3
""" Test Cases for the rectangle class. """
import unittest
import sys
import io
import pycodestyle
import os
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """ Test Cases for the rectangle class. """
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
        p = p8.check_files(['models/rectangle.py'])
        self.assertEqual(p.total_errors, 0, "fix pycodestyle")

    def test_pep8_test(self):
        """
        pep8 validation test
        """
        p8 = pycodestyle.StyleGuide(quiet=True)
        p = p8.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(p.total_errors, 0, "fix pycodestyle")

    def test_docstrings(self):
        """ test cases for documentations. """
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertIs(hasattr(Rectangle, "__init__"), True)
        self.assertIsNotNone(Rectangle.__init__.__doc__)
        self.assertIs(hasattr(Rectangle, "area"), True)
        self.assertIsNotNone(Rectangle.area.__doc__)
        self.assertIs(hasattr(Rectangle, "display"), True)
        self.assertIsNotNone(Rectangle.display.__doc__)
        self.assertIs(hasattr(Rectangle, "update"), True)
        self.assertIsNotNone(Rectangle.update.__doc__)
        self.assertIs(hasattr(Rectangle, "to_dictionary"), True)
        self.assertIsNotNone(Rectangle.to_dictionary.__doc__)

    def test_constructor_with_defaults(self):
        """ Test Cases for the rectangle class. """
        r1 = Rectangle(10, 2, 0, 0, 1)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_constructor_with_custom_id(self):
        """ Test Cases for the rectangle class. """
        r2 = Rectangle(2, 10, 0, 0, 33)
        self.assertEqual(r2.id, 33)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

    def test_constructor_with_all_arguments(self):
        """ Test Cases for the rectangle class. """
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

    def test_getters_and_setters(self):
        """ Test Cases for the rectangle class. """
        r4 = Rectangle(5, 5)
        r4.width = 7
        r4.height = 8
        r4.x = 1
        r4.y = 2
        self.assertEqual(r4.width, 7)
        self.assertEqual(r4.height, 8)
        self.assertEqual(r4.x, 1)
        self.assertEqual(r4.y, 2)

    def test_invalid_width_type(self):
        """ Test Cases for the rectangle class. """
        with self.assertRaises(TypeError) as context:
            r = Rectangle(10, "2")
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_negative_width_value(self):
        """ Test Cases for the rectangle class. """
        with self.assertRaises(ValueError) as context:
            r = Rectangle(-10, 2)
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_invalid_x_type(self):
        """ Test Cases for the rectangle class. """
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError) as context:
            r.x = {}
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_negative_x_value(self):
        """ Test Cases for the rectangle class. """
        with self.assertRaises(ValueError) as context:
            r = Rectangle(10, 2, -1)
        self.assertEqual(str(context.exception), "x must be >= 0")

    def test_invalid_y_type(self):
        """ Test Cases for the rectangle class. """
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError) as context:
            r.y = "invalid"
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_negative_y_value(self):
        """ Test Cases for the rectangle class. """
        with self.assertRaises(ValueError) as context:
            r = Rectangle(10, 2, 3, -1)
        self.assertEqual(str(context.exception), "y must be >= 0")

    def test_valid_attributes(self):
        """ Test Cases for the rectangle class. """
        r = Rectangle(10, 2)
        r.width = 5
        r.height = 3
        r.x = 2
        r.y = 1

    def test_invalid_height_type(self):
        """ Test Cases for the rectangle class. """
        with self.assertRaises(TypeError) as context:
            r = Rectangle(10, 2)
            r.height = "invalid"
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_negative_height_value(self):
        """ Test Cases for the rectangle class. """
        with self.assertRaises(ValueError) as context:
            r = Rectangle(10, 2)
            r.height = -3
        self.assertEqual(str(context.exception), "height must be > 0")

    def test_invalid_x_type_after_instantiation(self):
        """ Test Cases for the rectangle class. """
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError) as context:
            r.x = []
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_invalid_y_type_after_instantiation(self):
        """ Test Cases for the rectangle class. """
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError) as context:
            r.y = ()
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_area_method(self):
        """ Test Cases for the rectangle class. """
        r5 = Rectangle(5, 10)
        self.assertEqual(r5.area(), 50)

        r51 = Rectangle(3, 2)
        self.assertEqual(r51.area(), 6)

        r52 = Rectangle(2, 10)
        self.assertEqual(r52.area(), 20)

        r53 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r53.area(), 56)

    def test_area_method_with_changed_dimensions(self):
        """ Test Cases for the rectangle class. """
        r4 = Rectangle(5, 5)
        self.assertEqual(r4.area(), 25)
        r4.width = 8
        r4.height = 4
        self.assertEqual(r4.area(), 32)

    def test_area_method_with_negative_dimensions(self):
        """ Test Cases for the rectangle class. """
        r5 = Rectangle(3, 4)
        with self.assertRaises(ValueError) as context:
            r5.width = -3
        self.assertEqual(str(context.exception), "width must be > 0")

        with self.assertRaises(ValueError) as context:
            r5.height = -2
        self.assertEqual(str(context.exception), "height must be > 0")

    def test_area_method_with_zero_dimensions(self):
        """ Test Cases for the rectangle class. """
        r6 = Rectangle(7, 10)
        with self.assertRaises(ValueError) as context:
            r6.width = 0
        self.assertEqual(str(context.exception), "width must be > 0")

        with self.assertRaises(ValueError) as context:
            r6.height = 0
        self.assertEqual(str(context.exception), "height must be > 0")

    def test_display_method(self):
        """ Test Cases for the rectangle class. """
        r1 = Rectangle(4, 6)

        captured_output = io.StringIO()
        sys.stdout = captured_output

        r1.display()

        sys.stdout = sys.__stdout__

        expected_output = "####\n####\n####\n####\n####\n####\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_display_method_with_different_size(self):
        """ Test Cases for the rectangle class. """
        r2 = Rectangle(2, 2)

        captured_output = io.StringIO()
        sys.stdout = captured_output

        r2.display()

        sys.stdout = sys.__stdout__

        expected_output = "##\n##\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_display_method_with_single_character(self):
        """ Test Cases for the rectangle class. """
        r4 = Rectangle(1, 1)

        captured_output = io.StringIO()
        sys.stdout = captured_output

        r4.display()

        sys.stdout = sys.__stdout__

        expected_output = "#\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_display_method_with_position(self):
        """ Test Cases for the rectangle class. """
        r1 = Rectangle(2, 3, 2, 2)

        captured_output = io.StringIO()
        sys.stdout = captured_output

        r1.display()

        sys.stdout = sys.__stdout__

        expected_output = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_display_method_with_different_position(self):
        """ Test Cases for the rectangle class. """
        r2 = Rectangle(3, 2, 1, 0)

        captured_output = io.StringIO()
        sys.stdout = captured_output

        r2.display()

        sys.stdout = sys.__stdout__

        expected_output = " ###\n ###\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_display_method_with_no_position(self):
        """ Test Cases for the rectangle class. """
        r3 = Rectangle(3, 2)

        captured_output = io.StringIO()
        sys.stdout = captured_output

        r3.display()

        sys.stdout = sys.__stdout__

        expected_output = "###\n###\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_display_method_with_large_position(self):
        """ Test Cases for the rectangle class. """
        r4 = Rectangle(2, 2, 10, 5)

        captured_output = io.StringIO()
        sys.stdout = captured_output

        r4.display()

        sys.stdout = sys.__stdout__

        expected_output = "\n\n\n\n\n          ##\n          ##\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_str_method(self):
        """ Test Cases for the rectangle class. """
        r6 = Rectangle(3, 4, 1, 2, 5)
        self.assertEqual(str(r6), "[Rectangle] (5) 1/2 - 3/4")

    def test_update_method(self):
        """ Test Cases for the rectangle class. """
        r7 = Rectangle(2, 3)
        r7.update(1, 4, 5, 6, 7)
        self.assertEqual(r7.id, 1)
        self.assertEqual(r7.width, 4)
        self.assertEqual(r7.height, 5)
        self.assertEqual(r7.x, 6)
        self.assertEqual(r7.y, 7)

    def test_update_method(self):
        """ Test Cases for the rectangle class. """
        r1 = Rectangle(10, 10, 10, 10, 43)
        self.assertEqual(str(r1), "[Rectangle] (43) 10/10 - 10/10")

        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")

        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")

        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_method_with_kwargs(self):
        """ Test Cases for the rectangle class. """
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")

        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/1")

        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/10 - 1/1")

        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")

    def test_update_method_with_args_and_kwargs(self):
        """ Test Cases for the rectangle class. """
        r2 = Rectangle(5, 5)
        r2.update(2, height=2, width=3, y=1)
        self.assertEqual(str(r2), "[Rectangle] (2) 0/1 - 3/2")

    def test_update_method_with_empty_args(self):
        """ Test Cases for the rectangle class. """
        r3 = Rectangle(3, 3)
        r3.update(height=4, width=4, x=4, y=4, id=4)
        self.assertEqual(str(r3), "[Rectangle] (4) 4/4 - 4/4")

    def test_rectangle_to_dictionary(self):
        """ Test Cases for the rectangle class. """
        r1 = Rectangle(10, 2, 1, 9, 33)
        r1_dict = r1.to_dictionary()

        expected_dict = {'x': 1, 'y': 9, 'id': 33, 'height': 2, 'width': 10}
        self.assertDictEqual(r1_dict, expected_dict)

    def test_rectangle_from_dictionary(self):
        """ Test Cases for the rectangle class. """
        r1 = Rectangle(10, 2, 1, 9)
        r1_dict = r1.to_dictionary()

        r2 = Rectangle(1, 1)
        r2.update(**r1_dict)

        self.assertEqual(str(r1), str(r2))

    def test_rectangle_to_dictionary_type(self):
        """ Test Cases for the rectangle class. """
        r1 = Rectangle(10, 2, 1, 9)
        r1_dict = r1.to_dictionary()

        self.assertIsInstance(r1_dict, dict)

    def test_rectangle_to_dictionary_multiple_objects(self):
        """ Test Cases for the rectangle class. """
        r1 = Rectangle(10, 2, 1, 9, 4)
        r2 = Rectangle(5, 5, 0, 0, 2)
        r1_dict = r1.to_dictionary()
        r2_dict = r2.to_dictionary()

        expected_r1_dict = {'x': 1, 'y': 9, 'id': 4, 'height': 2, 'width': 10}
        expected_r2_dict = {'x': 0, 'y': 0, 'id': 2, 'height': 5, 'width': 5}

        self.assertDictEqual(r1_dict, expected_r1_dict)
        self.assertDictEqual(r2_dict, expected_r2_dict)


if __name__ == "__main__":
    unittest.main()
