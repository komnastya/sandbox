import unittest
from set import MySet


class TestMySet(unittest.TestCase):
    def test_add(self):
        s = MySet()
        self.assertEqual(list(s), [])
        s.add(1)
        s.add(11)
        self.assertEqual(sorted(list(s)), [1, 11])

    def test_clear(self):
        s = MySet()
        s.add(1)
        s.add(2)
        s.add(3)
        self.assertEqual(list(s), [1, 2, 3])

        s.clear()
        self.assertEqual(list(s), [])
        self.assertEqual(s.len, 0)

    def test_copy(self):
        a = MySet()

        a.add(1)
        a.add(2)
        a.add(3)

        self.assertEqual(list(a), [1, 2, 3])

        b = a.copy()

        a.add(4)
        b.remove(3)

        self.assertEqual(list(a), [1, 2, 3, 4])
        self.assertEqual(list(b), [1, 2])

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

    def test_remove(self):
        s = MySet()
        self.assertEqual(list(s), [])

        s.add(1)
        self.assertEqual(list(s), [1])

        s.remove(1)
        self.assertEqual(list(s), [])

        with self.assertRaises(KeyError):
            s.remove(2)

    def test_has(self):
        s = MySet()
        self.assertFalse(s.has(1))
        s.add(1)
        self.assertTrue(s.has(1))

    def test_equality(self):
        a = MySet()
        b = MySet()

        self.assertTrue(a == a)
        self.assertTrue(b == b)
        self.assertTrue(a == b)

        a.add(1)
        self.assertTrue(a != b)

        b.add(1)
        self.assertTrue(a == b)

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
        a = MySet()
        b = MySet()

        self.assertEqual(list(a.union(b)), [])

        for x in range(0, 4):
            a.add(x)

        self.assertEqual(list(a.union(b)), [0, 1, 2, 3])

        for x in range(2, 6):
            b.add(x)

        self.assertEqual(list(a.union(b)), [0, 1, 2, 3, 4, 5])

    def test_or_operator(self):
        a = MySet()
        b = MySet()

        self.assertEqual(list(a | b), [])

        for x in range(0, 4):
            a.add(x)

        self.assertEqual(list(a | b), [0, 1, 2, 3])

        for x in range(2, 6):
            b.add(x)

        self.assertEqual(list(a | b), [0, 1, 2, 3, 4, 5])

    def test_union_update(self):
        a = MySet()
        b = MySet()

        a.update(b)
        self.assertEqual(list(a), [])

        for x in range(0, 4):
            a.add(x)

        a.update(b)
        self.assertEqual(list(a), [0, 1, 2, 3])

        for x in range(2, 6):
            b.add(x)

        a.update(b)
        self.assertEqual(list(a), [0, 1, 2, 3, 4, 5])

        b.update(a)
        self.assertEqual(list(b), [0, 1, 2, 3, 4, 5])

    def test_ior_operator(self):
        a = MySet()
        b = MySet()

        for x in range(1, 5):
            a.add(x)

        for y in range(3, 8):
            b.add(y)

        a |= b
        self.assertEqual(list(a), [1, 2, 3, 4, 5, 6, 7])

        b |= a
        self.assertEqual(list(b), [1, 2, 3, 4, 5, 6, 7])

    def test_intersection(self):
        a = MySet()
        b = MySet()

        self.assertEqual(list(a.intersection(b)), [])

        for x in range(0, 4):
            a.add(x)

        self.assertEqual(list(a.intersection(b)), [])

        for x in range(2, 6):
            b.add(x)

        self.assertEqual(list(a.intersection(b)), [2, 3])

    def test_and_operator(self):
        a = MySet()
        b = MySet()

        self.assertEqual(list(a & b), [])

        for x in range(0, 4):
            a.add(x)

        self.assertEqual(list(a & b), [])

        for x in range(2, 6):
            b.add(x)

        self.assertEqual(list(a & b), [2, 3])

    def test_intersection_update(self):
        a = MySet()
        b = MySet()

        a.intersection_update(b)
        self.assertEqual(list(a), [])

        for x in range(0, 4):
            a.add(x)

        a.intersection_update(b)
        self.assertEqual(list(a), [])

        for x in range(0, 4):
            a.add(x)

        for x in range(2, 6):
            b.add(x)

        a.intersection_update(b)
        self.assertEqual(list(a), [2, 3])

        b.intersection_update(a)
        self.assertEqual(list(b), [2, 3])

    def test_iand_operator(self):
        a = MySet()
        b = MySet()

        a &= b
        self.assertEqual(list(a), [])

        for x in range(0, 4):
            a.add(x)

        a &= b
        self.assertEqual(list(a), [])

        for x in range(0, 4):
            a.add(x)

        for x in range(2, 6):
            b.add(x)

        a &= b
        self.assertEqual(list(a), [2, 3])

        b &= a
        self.assertEqual(list(b), [2, 3])

    def test_difference(self):
        a = MySet()
        b = MySet()

        self.assertEqual(list(a.difference(b)), [])

        for x in range(0, 4):
            a.add(x)

        self.assertEqual(list(a.difference(b)), [0, 1, 2, 3])

        for x in range(2, 6):
            b.add(x)

        self.assertEqual(list(a.difference(b)), [0, 1])
        self.assertEqual(list(b.difference(a)), [4, 5])

    def test_sub_operator(self):
        a = MySet()
        b = MySet()

        self.assertEqual(list(a - b), [])

        for x in range(0, 4):
            a.add(x)

        self.assertEqual(list(a - b), [0, 1, 2, 3])

        for x in range(2, 6):
            b.add(x)

        self.assertEqual(list(a - b), [0, 1])
        self.assertEqual(list(b - a), [4, 5])

    def test_difference_update(self):
        a = MySet()
        b = MySet()

        a.difference_update(b)
        self.assertEqual(list(a), [])

        for x in range(0, 4):
            a.add(x)

        a.difference_update(b)
        self.assertEqual(list(a), [0, 1, 2, 3])

        for x in range(2, 6):
            b.add(x)

        a.difference_update(b)
        self.assertEqual(list(a), [0, 1])

        a.difference_update(b)
        self.assertEqual(list(b), [2, 3, 4, 5])

    def test_isub_operator(self):
        a = MySet()
        b = MySet()

        a -= b
        self.assertEqual(list(a), [])

        for x in range(0, 4):
            a.add(x)

        a -= b
        self.assertEqual(list(a), [0, 1, 2, 3])

        for x in range(2, 6):
            b.add(x)

        a -= b
        self.assertEqual(list(a), [0, 1])

        b -= a
        self.assertEqual(list(b), [2, 3, 4, 5])

    def test_symmetric_difference(self):
        a = MySet()
        b = MySet()

        self.assertEqual(list(a.symmetric_difference(b)), [])

        for x in range(0, 4):
            a.add(x)

        self.assertEqual(list(a.symmetric_difference(b)), [0, 1, 2, 3])

        for x in range(2, 6):
            b.add(x)

        self.assertEqual(list(a.symmetric_difference(b)), [0, 1, 4, 5])

    def test_xor_operator(self):
        a = MySet()
        b = MySet()

        self.assertEqual(list(a ^ b), [])

        for x in range(0, 4):
            a.add(x)

        self.assertEqual(list(a ^ b), [0, 1, 2, 3])

        for x in range(2, 6):
            b.add(x)

        self.assertEqual(list(a ^ b), [0, 1, 4, 5])

    def test_ixor_operator(self):
        a = MySet()
        b = MySet()

        a ^= b
        self.assertEqual(list(a), [])

        for x in range(0, 4):
            a.add(x)

        a ^= b
        self.assertEqual(list(a), [0, 1, 2, 3])

        for x in range(2, 6):
            b.add(x)

        a ^= b
        self.assertEqual(list(a), [0, 1, 4, 5])

        b ^= a
        self.assertEqual(list(b), [0, 1])

    def test_isdisjoint(self):
        a = MySet()
        b = MySet()

        for x in range(11):
            a.add(x)

        for x in range(20, 29):
            b.add(x)

        self.assertTrue(a.isdisjoint(b))

        for x in range(1, 10):
            b.add(x)

        self.assertFalse(a.isdisjoint(b))

    def test_issubset(self):
        a = MySet()
        b = MySet()

        for x in range(3):
            a.add(x)

        self.assertFalse(a.issubset(b))

        for x in range(5):
            b.add(x)

        self.assertTrue(a.issubset(b))
        self.assertFalse(b.issubset(a))

    def test_issuperset(self):
        a = MySet()
        b = MySet()

        for x in range(7):
            a.add(x)

        self.assertTrue(a.issuperset(b))

        for x in range(3):
            b.add(x)

        self.assertTrue(a.issuperset(b))
        self.assertFalse(b.issuperset(a))
        self.assertTrue(b.issubset(a))


if __name__ == "__main__":
    unittest.main(exit=False)
