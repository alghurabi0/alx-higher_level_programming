#!/usr/bin/python3
""" Test Cases for the base class. """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import sys
import pycodestyle
from io import StringIO
import os


class TestBase(unittest.TestCase):
    """ Test Cases for the base class. """
    def setUp(self):
        """
        result to stdout
        """
        sys.stdout = StringIO()
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def tearDown(self):
        """
        clean up after execution
        """
        sys.stdout = sys.__stdout__
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_pep8_model(self):
        """
        pep8 validation test module
        """
        p8 = pycodestyle.StyleGuide(quiet=True)
        p = p8.check_files(['models/base.py'])
        self.assertEqual(p.total_errors, 0, "fix pycodestyle")

    def test_pep8_test(self):
        """
        pep8 validation test
        """
        p8 = pycodestyle.StyleGuide(quiet=True)
        p = p8.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(p.total_errors, 0, "fix pycodestyle")

    def test_docstrings(self):
        self.assertIsNotNone(Base.__doc__)
        self.assertIs(hasattr(Base, "__init__"), True)
        self.assertIsNotNone(Base.__init__.__doc__)
        self.assertIs(hasattr(Base, "create"), True)
        self.assertIsNotNone(Base.create.__doc__)
        self.assertIs(hasattr(Base, "to_json_string"), True)
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertIs(hasattr(Base, "from_json_string"), True)
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertIs(hasattr(Base, "save_to_file"), True)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIs(hasattr(Base, "load_from_file"), True)
        self.assertIsNotNone(Base.load_from_file.__doc__)

    def test_no_id_argument(self):
        """ Test Cases for the base class. """
        Base._Base__nb_objects = 0
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_with_id_argument(self):
        """ Test Cases for the base class. """
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_base_to_json_string_rectangle(self):
        """ Test Cases for the base class. """
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_string = Base.to_json_string([dictionary])

        expected_json_string = (
                '[{"x": 2, "width": 10, "id": 1, '
                '"height": 7, "y": 8}]'
        )
        self.assertEqual(json_string, expected_json_string)

    def test_base_to_json_string_square(self):
        """ Test Cases for the base class. """
        s1 = Square(5, 2, 1, 1)
        dictionary = s1.to_dictionary()
        json_string = Base.to_json_string([dictionary])

        expected_json_string = '[{"id": 1, "size": 5, "x": 2, "y": 1}]'
        self.assertEqual(json_string, expected_json_string)

    def test_base_to_json_string_multiple_objects(self):
        """ Test Cases for the base class. """
        r1 = Rectangle(10, 7, 2, 8, 1)
        s1 = Square(5, 2, 1, 2)
        r1_dict = r1.to_dictionary()
        s1_dict = s1.to_dictionary()
        json_string = Base.to_json_string([r1_dict, s1_dict])

        expected_json_string = (
                '[{"x": 2, "width": 10, "id": 1, '
                '"height": 7, "y": 8}, {"id": 2, "size": 5, "x": 2, "y": 1}]'
                )
        self.assertEqual(json_string, expected_json_string)

    def test_base_to_json_string_empty_list(self):
        """ Test Cases for the base class. """
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, '[]')

    def test_base_to_json_string_none(self):
        """ Test Cases for the base class. """
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, '[]')

    @classmethod
    def setUpClass(cls):
        """ Test Cases for the base class. """
        # Ensure the test files do not exist initially
        cls.remove_test_files()

    @classmethod
    def tearDownClass(cls):
        """ Test Cases for the base class. """
        # Clean up the test files after all tests are done
        cls.remove_test_files()

    @staticmethod
    def remove_test_files():
        """ Test Cases for the base class. """
        # Remove test files if they exist
        for filename in ["Rectangle.json", "Square.json"]:
            if os.path.exists(filename):
                os.remove(filename)

    def test_base_save_to_file_rectangle(self):
        """ Test Cases for the base class. """
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            json_content = file.read()

        expected_json = (
                '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}, '
                '{"x": 0, "width": 2, "id": 2, "height": 4, "y": 0}]'
                )
        self.assertEqual(json_content, expected_json)

    def test_base_save_to_file_square(self):
        """ Test Cases for the base class. """
        s1 = Square(5, 2, 1, 1)
        s2 = Square(3, 1, 0, 2)
        Square.save_to_file([s1, s2])

        with open("Square.json", "r") as file:
            json_content = file.read()

        expected_json = (
                '[{"id": 1, "size": 5, "x": 2, "y": 1}, '
                '{"id": 2, "size": 3, "x": 1, "y": 0}]'
                )
        self.assertEqual(json_content, expected_json)

    def test_base_save_to_file_empty_list(self):
        """ Test Cases for the base class. """
        Rectangle.save_to_file([])

        with open("Rectangle.json", "r") as file:
            json_content = file.read()

        self.assertEqual(json_content, "[]")

    def test_base_save_to_file_none(self):
        """ Test Cases for the base class. """
        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as file:
            json_content = file.read()

        self.assertEqual(json_content, "[]")

    def test_base_from_json_string_empty(self):
        """ Test Cases for the base class. """
        json_string = ''
        result = Rectangle.from_json_string(json_string)
        self.assertEqual(result, [])

    def test_base_from_json_string_none(self):
        """ Test Cases for the base class. """
        json_string = None
        result = Rectangle.from_json_string(json_string)
        self.assertEqual(result, [])

    def test_base_create(self):
        """ Test Cases for the base class. """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)

        self.assertEqual(r1.id, r2.id)
        self.assertEqual(r1.width, r2.width)
        self.assertEqual(r1.height, r2.height)
        self.assertEqual(r1.x, r2.x)
        self.assertEqual(r1.y, r2.y)

    def test_base_create_with_square(self):
        """ Test Cases for the base class. """
        s1 = Square(4)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)

        self.assertEqual(s1.id, s2.id)
        self.assertEqual(s1.width, s2.width)
        self.assertEqual(s1.height, s2.height)
        self.assertEqual(s1.x, s2.x)
        self.assertEqual(s1.y, s2.y)

    def test_base_create_with_missing_attributes(self):
        """ Test Cases for the base class. """
        valid_dict = {'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5}
        r = Rectangle.create(**valid_dict)

        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_empty_file(self):
        """ Test Cases for the base class. """
        Rectangle.save_to_file([])
        loaded_rectangles = Rectangle.load_from_file()
        self.assertEqual(loaded_rectangles, [], "Loading from an empty")

    def test_nonexistent_file(self):
        """ Test Cases for the base class. """
        loaded_squares = Square.load_from_file()
        self.assertEqual(loaded_squares, [], "Loading from a non-exis")

    def test_load_rectangles(self):
        """ Test Cases for the base class. """
        r1 = Rectangle(5, 5)
        Rectangle.save_to_file([r1])
        loaded_rectangles = Rectangle.load_from_file()
        self.assertIsInstance(loaded_rectangles, list)
        self.assertEqual(len(loaded_rectangles), 1)
        self.assertIsInstance(loaded_rectangles[0], Rectangle)

    def test_load_squares(self):
        """ Test Cases for the base class. """
        s1 = Square(2)
        s2 = Square(3, 1, 1)
        Square.save_to_file([s1, s2])
        loaded_squares = Square.load_from_file()
        self.assertIsInstance(loaded_squares, list, "Loading Squares failed")
        self.assertEqual(len(loaded_squares), 2, "Loading Squares failed")
        self.assertTrue(all(isinstance(obj, Square) for obj in loaded_squares))


if __name__ == "__main__":
    unittest.main()
