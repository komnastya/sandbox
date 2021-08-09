import unittest
from myiterators import head, skip, even, odd


class TestIterators(unittest.TestCase):
    def test_head(self):
        self.assertEqual(list(head([], 10)), [])
        self.assertEqual(list(head([1, 2, 3], 10)), [1, 2, 3])
        self.assertEqual(list(head([1, 2, 3], 0)), [])
        self.assertEqual(list(head([1, 2, 3, 4, 5, 6, 7, 8], 5)), [1, 2, 3, 4, 5])

    def test_skip(self):
        self.assertEqual(list(skip([], 10)), [])
        self.assertEqual(list(skip([1, 2, 3], 10)), [])
        self.assertEqual(list(skip([1, 2, 3], 0)), [1, 2, 3])
        self.assertEqual(list(skip([1, 2, 3, 4, 5], 3)), [4, 5])

    def test_even(self):
        self.assertEqual(list(even([])), [])
        self.assertEqual(list(even([1, 2, 3, 4])), [1, 3])

    def test_odd(self):
        self.assertEqual(list(odd([])), [])
        self.assertEqual(list(odd([1, 2, 3, 4])), [2, 4])

    def test_head_skip_odd_even_together(self):
        self.assertEqual(
            list(even(head([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6))), [0, 2, 4]
        )
        self.assertEqual(
            list(odd(head([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6))), [1, 3, 5]
        )
        self.assertEqual(
            list(even(skip([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))), [5, 7, 9]
        )
        self.assertEqual(
            list(odd(skip([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))), [6, 8, 10]
        )
        self.assertEqual(
            list(head(odd([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3)), [1, 3, 5]
        )
        self.assertEqual(
            list(head(even([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3)), [0, 2, 4]
        )
        self.assertEqual(list(skip(odd([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3)), [7, 9])
        self.assertEqual(
            list(skip(even([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3)), [6, 8, 10]
        )


if __name__ == "__main__":
    unittest.main()
