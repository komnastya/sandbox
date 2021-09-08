import unittest

from fibonacci import Fibonacci, fibonacci, fibonacci_g


class TestFibonacci(unittest.TestCase):
    def test_fibonacci_seq(self):
        self.assertEqual(fibonacci(1), [0, 1, 1])
        self.assertEqual(fibonacci(8), [0, 1, 1, 2, 3, 5, 8])
        self.assertEqual(fibonacci(15), [0, 1, 1, 2, 3, 5, 8, 13])
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_fibonacci_class(self):
        seq = Fibonacci()
        self.assertEqual(next(seq), 1)
        self.assertEqual(next(seq), 1)
        self.assertEqual(next(seq), 2)
        self.assertEqual(next(seq), 3)
        self.assertEqual(next(seq), 5)
        self.assertEqual(next(seq), 8)

    def test_fibonacci_generator(self):
        seq = fibonacci_g()
        self.assertEqual(next(seq), 1)
        self.assertEqual(next(seq), 1)
        self.assertEqual(next(seq), 2)
        self.assertEqual(next(seq), 3)
        self.assertEqual(next(seq), 5)
        self.assertEqual(next(seq), 8)


if __name__ == "__main__":
    unittest.main()
