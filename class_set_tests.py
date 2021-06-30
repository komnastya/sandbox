import unittest
from class_set import MySet


class TestNumberSetCalss(unittest.TestCase):
    def test_insert(self):
        s = MySet()
        self.assertEqual(list(s), [])
        s.add(1)
        s.add(11)
        self.assertEqual(sorted(list(s)), [1, 11])

    def test_insert_duplicates(self):
        s = MySet()
        self.assertEqual(list(s), [])
        s.add(1)
        s.add(1)
        s.add(1)
        self.assertEqual(sorted(list(s)), [1])

    def test_delete(self):
        s = MySet()
        self.assertFalse(s.has(1))
        s.delete(1)
        self.assertFalse(s.has(1))
        s.add(1)
        self.assertTrue(s.has(1))
        s.delete(1)
        self.assertFalse(s.has(1))

    def test_has(self):
        s = MySet()
        self.assertFalse(s.has(1))
        s.add(1)
        self.assertTrue(s.has(1))

    def test_iterator(self):
        s = MySet()
        s.add(1)
        s.add(2)
        s.add(3)
        self.assertEqual(sorted(list(s)), [1, 2, 3])

    def test_len(self):
        s = MySet()
        self.assertEqual(len(s), 0)
        s.add(1)
        s.add(2)
        s.add(3)
        self.assertEqual(len(s), 3)
        s.delete(3)
        self.assertEqual(len(s), 2)

    def test_str(self):
        s = MySet()
        self.assertEqual(str(s), "{}")
        s.add(1)
        s.add(2)
        s.add(3)

        self.assertEqual(str(s), "{1, 2, 3}")

    def test_union(self):
        set_one = MySet()
        set_two = MySet()

        self.assertEqual(list(set_one.union(set_two)), [])

        for x in range(0, 4):
            set_one.add(x)

        self.assertEqual(list(set_one.union(set_two)), [0, 1, 2, 3])

        for x in range(2, 6):
            set_two.add(x)

        self.assertEqual(list(set_one.union(set_two)), [0, 1, 2, 3, 4, 5])

    def test_intersection(self):
        set_one = MySet()
        set_two = MySet()

        self.assertEqual(list(set_one.intersection(set_two)), [])

        for x in range(0, 4):
            set_one.add(x)

        self.assertEqual(list(set_one.intersection(set_two)), [])

        for x in range(2, 6):
            set_two.add(x)

        self.assertEqual(list(set_one.intersection(set_two)), [2, 3])

    def test_difference(self):
        set_one = MySet()
        set_two = MySet()

        self.assertEqual(list(set_one.difference(set_two)), [])

        for x in range(0, 4):
            set_one.add(x)

        self.assertEqual(list(set_one.difference(set_two)), [0, 1, 2, 3])

        for x in range(2, 6):
            set_two.add(x)

        self.assertEqual(list(set_one.difference(set_two)), [0, 1])
        self.assertEqual(list(set_two.difference(set_one)), [4, 5])

    def test_symmetric_diff(self):
        set_one = MySet()
        set_two = MySet()

        self.assertEqual(list(set_one.symmetric_diff(set_two)), [])

        for x in range(0, 4):
            set_one.add(x)

        self.assertEqual(list(set_one.symmetric_diff(set_two)), [0, 1, 2, 3])

        for x in range(2, 6):
            set_two.add(x)

        self.assertEqual(list(set_one.symmetric_diff(set_two)), [0, 1, 4, 5])


if __name__ == "__main__":
    unittest.main(exit=False)
