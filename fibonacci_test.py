import unittest
from fibonacci import Fibonacci, fibonacci


class TestFibonacci(unittest.TestCase):
    def test_fibinacci_class(self):
        seq = Fibonacci()
        self.assertEqual(next(seq), 1)
        self.assertEqual(next(seq), 1)
        self.assertEqual(next(seq), 2)
        self.assertEqual(next(seq), 3)
        self.assertEqual(next(seq), 5)
        self.assertEqual(next(seq), 8)

    def test_fibonacci_function(self):
        seq = fibonacci()
        self.assertEqual(next(seq), 1)
        self.assertEqual(next(seq), 1)
        self.assertEqual(next(seq), 2)
        self.assertEqual(next(seq), 3)
        self.assertEqual(next(seq), 5)
        self.assertEqual(next(seq), 8)


if __name__ == "__main__":
    unittest.main()
