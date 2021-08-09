import unittest
from triangle_iterator import triangle


class TestTriangle(unittest.TestCase):
    def test_finite_iterator_of_iterators(self):
        finite_iterator = iter(triangle(3))
        list_of_lists = [list(inner_iterator) for inner_iterator in finite_iterator]
        self.assertEqual(list_of_lists, [[], [1], [1, 2]])

    def test_empty_iterator(self):
        finite_iterator = iter(triangle(0))
        self.assertEqual(list(finite_iterator), [])

    def test_infinite_iterator_of_iterators(self):
        infinite_iterator = iter(triangle())
        self.assertEqual(list(next(infinite_iterator)), [])
        self.assertEqual(list(next(infinite_iterator)), [1])
        self.assertEqual(list(next(infinite_iterator)), [1, 2])
        self.assertEqual(list(next(infinite_iterator)), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
