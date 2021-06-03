import unittest
from pushback import PushBackIterator


class TestMerge(unittest.TestCase):
    def test_push_back_iterator(self):
        numbers = PushBackIterator(iter([1, 2, 3, 4, 5]))
        self.assertEqual(next(numbers), 1)
        self.assertEqual(next(numbers), 2)
        self.assertEqual(next(numbers), 3)
        self.assertEqual(next(numbers), 4)
        self.assertEqual(next(numbers), 5)

    def test_push_back_method(self):
        numbers = PushBackIterator(iter([3, 4, 5]))
        self.assertEqual(next(numbers), 3)

        numbers.push_back(3)
        self.assertEqual(next(numbers), 3)

        numbers.push_back(3)
        numbers.push_back(2)
        numbers.push_back(1)
        self.assertEqual(list(numbers), [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
