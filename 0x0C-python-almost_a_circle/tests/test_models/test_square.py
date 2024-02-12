#!/usr/bin/python3

""" Square test """


import unittest
import os
from models.square import Square


class TestSquare(unittest.TestCase):
    def setUp(self):
        """ Create some instances for testing """
        self.square1 = Square(5)
        self.square2 = Square(7, 2, 2, 1)

        """ Save instances to files """
        Square.save_to_file([self.square1, self.square2])

    def test_load_from_file_exists(self):
        """ Test if the file exists """
        self.assertTrue(os.path.exists('Square.json'))

    def test_load_from_file_nonempty(self):
        """ Test loading from existing file """
        squares = Square.load_from_file()

        """ Ensure correct number of squares loaded """
        self.assertEqual(len(squares), 2)

        """ Ensure squares have correct attributes """
        self.assertEqual(squares[0].size, 5)
        self.assertEqual(squares[0].x, 0)
        self.assertEqual(squares[0].y, 0)
        self.assertEqual(squares[1].size, 7)
        self.assertEqual(squares[1].x, 2)
        self.assertEqual(squares[1].y, 2)
        self.assertEqual(squares[1].id, 1)

    def test_update(self):
        """ Test updating square attributes """
        self.square1.update(1, 10, 2, 2)
        self.assertEqual(self.square1.size, 10)
        self.assertEqual(self.square1.x, 2)
        self.assertEqual(self.square1.y, 2)
        self.assertEqual(self.square1.id, 1)

    def test_area(self):
        """ Test calculating square area """
        self.assertEqual(self.square1.area(), 25)
        self.assertEqual(self.square2.area(), 49)

if __name__ == '__main__':
    unittest.main()
