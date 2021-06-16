import unittest
from ranges import MyRange, my_range


class TestRanges(unittest.TestCase):
    def test_myrange_class_initialization(self):
        nums = MyRange(1, 6)
        self.assertEqual(list(nums), [1, 2, 3, 4, 5])

        nums = MyRange(1, 1)
        self.assertEqual(list(nums), [])


    def test_next_method(self):
        nums = MyRange(1, 4)

        next(nums)
        next(nums)
        next(nums)

        with self.assertRaises(StopIteration):
            next(nums)

    def test_my_range_function(self):
        self.assertEqual(list(my_range(1, 4)), [1, 2, 3])
        self.assertEqual(list(my_range(4, 1)), [])


if __name__ == "__main__":
    unittest.main()
