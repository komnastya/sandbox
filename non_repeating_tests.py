import unittest
from non_repeating import non_repeating_one, non_repeating_two, non_repeating_better


class TestNonRepeating(unittest.TestCase):
    def test_non_repeating_one(self):
        self.assertEqual(list(non_repeating_one([])), [])
        self.assertEqual(list(non_repeating_one([1, 2, 3, 4, 5])), [1, 2, 3, 4, 5])
        self.assertEqual(list(non_repeating_one([1, 2, 1, 2, 1])), [1, 2, 1, 2, 1])
        self.assertEqual(list(non_repeating_one([1, 1, 1, 1, 1])), [1])
        self.assertEqual(list(non_repeating_one([1, 1, 2, 2, 2])), [1, 2])
        self.assertEqual(
            list(non_repeating_one([1, 2, 2, 3, 4, 4, 5, 6, 6])), [1, 2, 3, 4, 5, 6]
        )

    def test_non_repeating_two(self):
        self.assertEqual(list(non_repeating_two([])), [])
        self.assertEqual(list(non_repeating_two([1, 2, 3, 4, 5])), [1, 2, 3, 4, 5])
        self.assertEqual(list(non_repeating_two([1, 2, 1, 2, 1])), [1, 2, 1, 2, 1])
        self.assertEqual(list(non_repeating_two([1, 1, 1, 1, 1])), [1])
        self.assertEqual(list(non_repeating_two([1, 1, 2, 2, 2])), [1, 2])
        self.assertEqual(
            list(non_repeating_two([1, 2, 2, 3, 4, 4, 5, 6, 6])), [1, 2, 3, 4, 5, 6]
        )

    def test_non_repeating_better(self):
        self.assertEqual(list(non_repeating_better([])), [])
        self.assertEqual(list(non_repeating_better([None, None, None])),
                         [None])
        self.assertEqual(list(non_repeating_better([1, 2, 3, 4, 5])),
                         [1, 2, 3, 4, 5])
        self.assertEqual(list(non_repeating_better([1, 2, 1, 2, 1])),
                         [1, 2, 1, 2, 1])
        self.assertEqual(list(non_repeating_better([1, 1, 1, 1, 1])), [1])
        self.assertEqual(list(non_repeating_better([1, 1, 2, 2, 2])), [1, 2])
        self.assertEqual(list(non_repeating_better([1, 2, 2, 3, 4, 4, 5, 6, 6])),
                         [1, 2, 3, 4, 5, 6])



if __name__ == "__main__":
    unittest.main()
