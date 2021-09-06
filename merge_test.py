import unittest

from merge import merge, merge_better, merge_ugly


class TestMerge(unittest.TestCase):
    def test_merge(self):
        self.assertEqual(list(merge([], [])), [])
        self.assertEqual(list(merge([1, 1, 1], [])), [1, 1, 1])
        self.assertEqual(list(merge([], [2, 2, 2])), [2, 2, 2])
        self.assertEqual(list(merge([2, 4, 6], [1, 3, 5])), [1, 2, 3, 4, 5, 6])
        self.assertEqual(list(merge([1, 3, 5], [2, 4, 6])), [1, 2, 3, 4, 5, 6])
        self.assertEqual(list(merge([1, 1, 1], [2, 2, 2])), [1, 1, 1, 2, 2, 2])
        self.assertEqual(list(merge([2, 2, 2], [1, 1, 1])), [1, 1, 1, 2, 2, 2])

    def test_merge_better(self):
        self.assertEqual(list(merge_better([], [])), [])
        self.assertEqual(list(merge_better([1, 1, 1], [])), [1, 1, 1])
        self.assertEqual(list(merge_better([], [2, 2, 2])), [2, 2, 2])
        self.assertEqual(list(merge_better([2, 4, 6], [1, 3, 5])), [1, 2, 3, 4, 5, 6])
        self.assertEqual(list(merge_better([1, 3, 5], [2, 4, 6])), [1, 2, 3, 4, 5, 6])
        self.assertEqual(list(merge_better([1, 1, 1], [2, 2, 2])), [1, 1, 1, 2, 2, 2])
        self.assertEqual(list(merge_better([2, 2, 2], [1, 1, 1])), [1, 1, 1, 2, 2, 2])

    def test_merge_ugly(self):
        self.assertEqual(list(merge_ugly([], [])), [])
        self.assertEqual(list(merge_ugly([1, 1, 1], [])), [1, 1, 1])
        self.assertEqual(list(merge_ugly([], [2, 2, 2])), [2, 2, 2])
        self.assertEqual(list(merge_ugly([2, 4, 6], [1, 3, 5])), [1, 2, 3, 4, 5, 6])
        self.assertEqual(list(merge_ugly([1, 3, 5], [2, 4, 6])), [1, 2, 3, 4, 5, 6])
        self.assertEqual(list(merge_ugly([1, 1, 1], [2, 2, 2])), [1, 1, 1, 2, 2, 2])
        self.assertEqual(list(merge_ugly([2, 2, 2], [1, 1, 1])), [1, 1, 1, 2, 2, 2])


if __name__ == "__main__":
    unittest.main()
