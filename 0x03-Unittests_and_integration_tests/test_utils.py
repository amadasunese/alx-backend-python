#!/usr/bin/env python3
""" Parameterize a unit test, Mock HTTP calls, Parameterize and patch """
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ Test Case for function access_nested_map """

    # Tests for normal inputs and expected results
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test the access_nested_map function from a utils module
        """
        # Call the function with the provided arguments
        result = access_nested_map(nested_map, path)

        # Assert that the returned value matches the expected value
        self.assertEqual(result, expected)

    # Tests for inputs that should raise exceptions
    @parameterized.expand([
        ({}, ("a",), "Key not found: 'a'"),
        ({"a": 1}, ("a", "b"), "Key not found: 'b'"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_message):
        """
        Test that a KeyError is raised for invalid path access in the nested map
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)

        # Check that the exception message is as expected
        self.assertEqual(str(cm.exception), expected_message)


# This allows running the tests from the command line
if __name__ == "__main__":
    unittest.main()
