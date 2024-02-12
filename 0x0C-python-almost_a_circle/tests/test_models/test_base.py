#!/usr/bin/python3

""" Testing base """


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def setUp(self):
        """ Create some instances for testing """
        self.rectangle_instance = Base.create(width=5, height=10)
        self.square_instance = Base.create(size=7)

        """ Save instances to files """
        Base.save_to_file([self.rectangle_instance, self.square_instance])

    def test_load_from_file_nonempty(self):
        """ Test loading from existing files """
        instances = Bases.load_from_file()

        """ Ensure correct number of instances loaded """
        self.assertEqual(len(instances), 2)

        """
        Ensure instances are of correct types and have correct attributes
        """
        self.assertequalIsInstance(instances[0], type(self.rectangle_instance))
        self.assertEqual(instances[0].width, 5)
        self.assertEqual(instances[0].height, 10)
        self.assertIsInstance(instances[1], type(self.square_instance))
        self.assertEqual(instances[1].size, 7)

    def test_create_rectangle(self):
        """ Test creating a square instance """
        square = Base.create(size=5)
        self.assertEqual(square.size, 5)

    def test_to_json_string(self):
        """ Test conversion to JSON string """
        dictionary = [{'width': 5, 'height': 10}, {'size': 7}]
        json_string = Base.to_json_string(dictionary)
        self.assertEqual(json_string, '[{"width": 5, "height": 10},
        {"size": 7}]')

    def test_from_json_string(self):
        """ Test conversion from JSON string """
        json_string = '[{"width": 5, "height": 10}, {"size": 7}]'
        dictionary = Base.from_json_string(json_string)
        self.assertEqual(dictionary, [{'width': 5, 'height': 10}, {'size': 7}])

if __name__ == '__main__':
    unittest.main()
