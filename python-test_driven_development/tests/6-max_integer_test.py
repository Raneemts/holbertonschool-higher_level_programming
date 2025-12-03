#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_ordered_list(self):
        """Test max of an ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test max of an unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test list where the max is the first element"""
        self.assertEqual(max_integer([10, 2, 3]), 10)

    def test_max_in_middle(self):
        """Test max in the middle"""
        self.assertEqual(max_integer([1, 5, 2]), 5)

    def test_one_element(self):
        """Test a list with one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test list with negative numbers"""
        self.assertEqual(max_integer([-5, -2, -9]), -2)

    def test_mixed_signs(self):
        """Test list with both positive and negative numbers"""
        self.assertEqual(max_integer([-3, 7, 2, -8]), 7)

    def test_all_same(self):
        """Test list where all numbers are equal"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_floats(self):
        """Test list with floats"""
        self.assertEqual(max_integer([1.5, 2.8, 2.7]), 2.8)

    def test_mixed_int_float(self):
        """Test list with int and float mix"""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_string(self):
        """Test a string input (max char lexicographically)"""
        self.assertEqual(max_integer("hello"), 'o')

    def test_list_of_strings(self):
        """Test a list of strings (max lexicographically)"""
        self.assertEqual(max_integer(["abc", "xyz", "def"]), "xyz")


if __name__ == '__main__':
    unittest.main()
