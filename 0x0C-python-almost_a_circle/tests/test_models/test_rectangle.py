#!/usr/bin/python3

""" Rectangle test """


import unittest
import os
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        """ Create some instances for testing """
        self.rectangle1 = Rectangle(5, 10)
        self.rectangle2 = Rectangle(7, 3, 2, 2, 1)

        """ Save instances to files """
        Rectangle.save_to_file([self.rectangle1, self.rectangle2])

    def test_load_from_file_exists(self):
        """ Test if the file exists """
        self.assertTrue(os.path.exists('Rectangle.json'))

    def test_load_from_file_empty(self):
        """ Remove the test file """
        os.remove('Rectangle.json')

        """ Test loading from non-existent file """
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_nonempty(self):
        """ Test loading from existing file """
        rectangles = Rectangle.load_from_file()

        """ Ensure correct number of rectangles loaded """
        self.assertEqual(len(rectangles), 2)

        """ Ensure rectangles have correct attributes """
        self.assertEqual(rectangles[0].width, 5)
        self.assertEqual(rectangles[0].height, 10)
        self.assertEqual(rectangles[0].x, 0)
        self.assertEqual(rectangles[0].y, 0)
        self.assertEqual(rectangles[1].width, 7)
        self.assertEqual(rectangles[1].height, 3)
        self.assertEqual(rectangles[1].x, 2)
        self.assertEqual(rectangles[1].y, 2)
        self.assertEqual(rectangles[1].id, 1)

    def test_update(self):
        """ Test updating rectangle attributes """
        self.rectangle1.update(1, 10, 15, 2, 2)
        self.assertEqual(self.rectangle1.width, 10)
        self.assertEqual(self.rectangle1.height, 15)
        self.assertEqual(self.rectangle1.x, 2)
        self.assertEqual(self.rectangle1.y, 2)
        self.assertEqual(self.rectangle1.id, 1)

    def test_area(self):
        """ Test calculating rectangle area """
        self.assertEqual(self.rectangle1.area(), 50)
        self.assertEqual(self.rectangle2.area(), 21)


if __name__ == '__main__':
    unittest.main()
