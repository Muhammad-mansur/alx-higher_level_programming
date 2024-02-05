#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_all(self):
        self.assertEqual(max_integer([3, 5]), 5)
        self.assertEqual(max_integer((3, 5)), 5)
        self.assertEqual(max_integer('aeth'), 't')
        self.assertEqual(max_integer('a'), 'a')
        self.assertRaises(TypeError, max_integer, 5)
        self.assertRaises(TypeError, max_integer, False)
        self.assertRaises(TypeError, max_integer, {3, 5})
        self.assertEqual(max_integer([[5, 4, 1], [6, 3], []]), [6, 3])
        self.assertEqual(max_integer([(5, 4, 1), (6, 3), ()]), (6, 3))
        self.assertEqual(max_integer(['azzz', 'byy', 'cx']), 'cx')
        self.assertEqual(max_integer([{5, 4}, {6, 3, 1}, {20}]), {4, 5})
        self.assertRaises(TypeError, max_integer, (5))
        self.assertEqual(max_integer(''), None)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(()), None)
