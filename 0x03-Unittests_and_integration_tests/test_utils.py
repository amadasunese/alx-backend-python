#!/usr/bin/env python3
""" Parameterize a unit test, Mock HTTP calls, Parameterize and patch """

import unittest
from parameterized import parameterized
from utils import access_nested_map  # Import the function from your utils module

class TestAccessNestedMap(unittest.TestCase):
    """ Test Case"""
    """to test the function for following inputs """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),  # expected value is 1
        ({"a": {"b": 2}}, ("a",), {"b": 2}),  # expected value is {"b": 2}
        ({"a": {"b": 2}}, ("a", "b"), 2),  # expected value is 2
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test the access_nested_map function from a utils module
        """
        # Call the function with the provided arguments
        result = access_nested_map(nested_map, path)

        # Assert that the returned value matches the expected value
        self.assertEqual(result, expected)

# This allows running the tests from the command line
if __name__ == "__main__":
    unittest.main()
