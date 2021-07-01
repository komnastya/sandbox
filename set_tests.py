import unittest
from set import MySet


class TestMySet(unittest.TestCase):
    def test_insert(self):
        s = MySet()
        self.assertEqual(list(s), [])
        s.add(1)
        s.add(11)
        self.assertEqual(sorted(list(s)), [1, 11])

    def test_add_duplicates(self):
        s = MySet()
        self.assertEqual(list(s), [])
        s.add(1)
        s.add(1)
        s.add(1)
        self.assertEqual(sorted(list(s)), [1])

    def test_discard(self):
        s = MySet()
        self.assertFalse(s.has(1))
        s.discard(1)
        self.assertFalse(s.has(1))
        s.add(1)
        self.assertTrue(s.has(1))
        s.discard(1)
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
        s.discard(3)
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

    def test_or_operator(self):
        set_one = MySet()
        set_two = MySet()

        self.assertEqual(list(set_one | set_two), [])

        for x in range(0, 4):
            set_one.add(x)

        self.assertEqual(list(set_one | set_two), [0, 1, 2, 3])

        for x in range(2, 6):
            set_two.add(x)

        self.assertEqual(list(set_one | set_two), [0, 1, 2, 3, 4, 5])

    def test_union_update(self):
        set_one = MySet()
        set_two = MySet()

        set_one.update(set_two)
        self.assertEqual(list(set_one), [])

        for x in range(0, 4):
            set_one.add(x)

        set_one.update(set_two)
        self.assertEqual(list(set_one), [0, 1, 2, 3])

        for x in range(2, 6):
            set_two.add(x)

        set_one.update(set_two)
        self.assertEqual(list(set_one), [0, 1, 2, 3, 4, 5])

        set_two.update(set_one)
        self.assertEqual(list(set_two), [0, 1, 2, 3, 4, 5])

    def test_ior_operator(self):
        set_one = MySet()
        set_two = MySet()

        for x in range(1, 5):
            set_one.add(x)

        for y in range(3, 8):
            set_two.add(y)

        set_one |= set_two
        self.assertEqual(list(set_one), [1, 2, 3, 4, 5, 6, 7])

        set_two |= set_one
        self.assertEqual(list(set_two), [1, 2, 3, 4, 5, 6, 7])

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

    def test_and_operator(self):
        set_one = MySet()
        set_two = MySet()

        self.assertEqual(list(set_one & set_two), [])

        for x in range(0, 4):
            set_one.add(x)

        self.assertEqual(list(set_one & set_two), [])

        for x in range(2, 6):
            set_two.add(x)

        self.assertEqual(list(set_one & set_two), [2, 3])

    def test_intersection_update(self):
        set_one = MySet()
        set_two = MySet()

        set_one.intersection_update(set_two)
        self.assertEqual(list(set_one), [])

        for x in range(0, 4):
            set_one.add(x)

        set_one.intersection_update(set_two)
        self.assertEqual(list(set_one), [])

        for x in range(0, 4):
            set_one.add(x)

        for x in range(2, 6):
            set_two.add(x)

        set_one.intersection_update(set_two)
        self.assertEqual(list(set_one), [2, 3])

        set_two.intersection_update(set_one)
        self.assertEqual(list(set_two), [2, 3])

    def test_iand_operator(self):
        set_one = MySet()
        set_two = MySet()

        set_one &= set_two
        self.assertEqual(list(set_one), [])

        for x in range(0, 4):
            set_one.add(x)

        set_one &= set_two
        self.assertEqual(list(set_one), [])

        for x in range(0, 4):
            set_one.add(x)

        for x in range(2, 6):
            set_two.add(x)

        set_one &= set_two
        self.assertEqual(list(set_one), [2, 3])

        set_two &= set_one
        self.assertEqual(list(set_two), [2, 3])

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

    def test_sub_operator(self):
        set_one = MySet()
        set_two = MySet()

        self.assertEqual(list(set_one - set_two), [])

        for x in range(0, 4):
            set_one.add(x)

        self.assertEqual(list(set_one - set_two), [0, 1, 2, 3])

        for x in range(2, 6):
            set_two.add(x)

        self.assertEqual(list(set_one - set_two), [0, 1])
        self.assertEqual(list(set_two - set_one), [4, 5])

    def test_difference_update(self):
        set_one = MySet()
        set_two = MySet()

        set_one.difference_update(set_two)
        self.assertEqual(list(set_one), [])

        for x in range(0, 4):
            set_one.add(x)

        set_one.difference_update(set_two)
        self.assertEqual(list(set_one), [0, 1, 2, 3])

        for x in range(2, 6):
            set_two.add(x)

        set_one.difference_update(set_two)
        self.assertEqual(list(set_one), [0, 1])

        set_one.difference_update(set_two)
        self.assertEqual(list(set_two), [2, 3, 4, 5])

    def test_isub_operator(self):
        set_one = MySet()
        set_two = MySet()

        set_one -= set_two
        self.assertEqual(list(set_one), [])

        for x in range(0, 4):
            set_one.add(x)

        set_one -= set_two
        self.assertEqual(list(set_one), [0, 1, 2, 3])

        for x in range(2, 6):
            set_two.add(x)

        set_one -= set_two
        self.assertEqual(list(set_one), [0, 1])

        set_two -= set_one
        self.assertEqual(list(set_two), [2, 3, 4, 5])

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

    def test_xor_operator(self):
        set_one = MySet()
        set_two = MySet()

        self.assertEqual(list(set_one ^ set_two), [])

        for x in range(0, 4):
            set_one.add(x)

        self.assertEqual(list(set_one ^ set_two), [0, 1, 2, 3])

        for x in range(2, 6):
            set_two.add(x)

        self.assertEqual(list(set_one ^ set_two), [0, 1, 4, 5])

    def test_ixor_operator(self):
        set_one = MySet()
        set_two = MySet()

        set_one ^= set_two
        self.assertEqual(list(set_one), [])

        for x in range(0, 4):
            set_one.add(x)

        set_one ^= set_two
        self.assertEqual(list(set_one), [0, 1, 2, 3])

        for x in range(2, 6):
            set_two.add(x)

        set_one ^= set_two
        self.assertEqual(list(set_one), [0, 1, 4, 5])

        set_two ^= set_one
        self.assertEqual(list(set_two), [0, 1])

    def test_isdisjoint(self):
        set_one = MySet()
        set_two = MySet()

        for x in range(11):
            set_one.add(x)

        for x in range(20, 29):
            set_two.add(x)

        self.assertTrue(set_one.isdisjoint(set_two))

        for x in range(1, 10):
            set_two.add(x)

        self.assertFalse(set_one.isdisjoint(set_two))

    def test_issubset(self):
        set_one = MySet()
        set_two = MySet()

        for x in range(3):
            set_one.add(x)

        self.assertFalse(set_one.issubset(set_two))

        for x in range(5):
            set_two.add(x)

        self.assertTrue(set_one.issubset(set_two))
        self.assertFalse(set_two.issubset(set_one))

    def test_issuperset(self):
        set_one = MySet()
        set_two = MySet()

        for x in range(7):
            set_one.add(x)

        self.assertTrue(set_one.issuperset(set_two))

        for x in range(3):
            set_two.add(x)

        self.assertTrue(set_one.issuperset(set_two))
        self.assertFalse(set_two.issuperset(set_one))
        self.assertTrue(set_two.issubset(set_one))


if __name__ == "__main__":
    unittest.main(exit=False)
