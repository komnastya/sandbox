import unittest
from non_repeating import non_repeating


class TestNonRepeating(unittest.TestCase):
    def test_non_repeating(self):
        self.assertEqual(list(non_repeating([])), [])
        self.assertEqual(list(non_repeating([1, 2, 3, 4, 5])), [1, 2, 3, 4, 5])
        self.assertEqual(list(non_repeating([1, 2, 1, 2, 1])), [1, 2, 1, 2, 1])
        self.assertEqual(list(non_repeating([1, 1, 1, 1, 1])), [1])
        self.assertEqual(list(non_repeating([1, 1, 2, 2, 2])), [1, 2])
        self.assertEqual(
            list(non_repeating([1, 2, 2, 3, 4, 4, 5, 6, 6])), [1, 2, 3, 4, 5, 6]
        )


if __name__ == "__main__":
    unittest.main()
