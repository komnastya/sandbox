import unittest
from unique import unique


class TestUnique(unittest.TestCase):
    def test_unique(self):
        self.assertEqual(list(unique([])), [])
        self.assertEqual(list(unique([1, 2, 3, 4, 5])), [1, 2, 3, 4, 5])
        self.assertEqual(list(unique([1, 2, 1, 2, 1])), [1, 2])
        self.assertEqual(list(unique([1, 1, 1, 1, 1])), [1])
        self.assertEqual(list(unique([1, 1, 2, 2, 2])), [1, 2])


if __name__ == "__main__":
    unittest.main()
