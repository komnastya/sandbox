import unittest
from merge_lists import merge_lists


class TestMergeLists(unittest.TestCase):
    def test_merge(self):
        self.assertEqual(merge_lists([], []), [])
        self.assertEqual(merge_lists([1, 1, 1], []), [1, 1, 1])
        self.assertEqual(merge_lists([], [2, 2, 2]), [2, 2, 2])
        self.assertEqual(merge_lists([2, 4, 6], [1, 3, 5]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge_lists([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge_lists([1, 1, 1], [2, 2, 2]), [1, 1, 1, 2, 2, 2])
        self.assertEqual(merge_lists([2, 2, 2], [1, 1, 1]), [1, 1, 1, 2, 2, 2])


if __name__ == "__main__":
    unittest.main()
