import unittest
from binarysearch import binary_search


class TestBinarySearch(unittest.TestCase):
    def test_binarysearch(self):
        self.assertEqual(binary_search([0, 1, 2, 3, 4, 5], 5), 5)
        self.assertEqual(binary_search([0, 1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(binary_search([], 1), -1)


if __name__ == "__main__":
    unittest.main()
