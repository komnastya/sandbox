import unittest
from pushback import PushBackIterator


class TestMerge(unittest.TestCase):
    def test_push_back_iterator(self):
        nums = PushBackIterator(iter([1, 2, 3, 4, 5]))
        self.assertEqual(list(nums), [1, 2, 3, 4, 5])

    def test_push_back_method(self):
        nums = PushBackIterator(iter([3, 4, 5]))
        self.assertEqual(next(nums), 3)

        nums.push_back(3)
        self.assertEqual(next(nums), 3)

        nums.push_back(3)
        nums.push_back(2)
        nums.push_back(1)
        self.assertEqual(list(nums), [1, 2, 3, 4, 5])

    def test_has_next_method(self):
        nums = PushBackIterator(iter([]))
        self.assertFalse(nums.has_next())

        nums = PushBackIterator(iter([1, 2, 3]))
        self.assertEqual(next(nums), 1)

        self.assertTrue(nums.has_next())
        self.assertEqual(next(nums), 2)

        self.assertTrue(nums.has_next())
        self.assertEqual(next(nums), 3)

        self.assertFalse(nums.has_next())

    def test_has_next_and_push_back_methods_together(self):
        nums = PushBackIterator(iter([3, 4]))

        self.assertEqual(next(nums), 3)
        self.assertEqual(next(nums), 4)

        self.assertFalse(nums.has_next())

        nums.push_back(5)
        self.assertTrue(nums.has_next())

        self.assertEqual(next(nums), 5)
        self.assertFalse(nums.has_next())

        nums = PushBackIterator(iter([]))
        self.assertFalse(nums.has_next())
        nums.push_back(1)
        self.assertEqual(list(nums), [1])


if __name__ == "__main__":
    unittest.main()
