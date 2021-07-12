import unittest
from dict import MyDict


class TestMyDict(unittest.TestCase):
    def test_dictionary(self):
        d = MyDict()
        d.set(1, "one")
        d.set(2, "two")
        d.set(3, "three")

        self.assertEqual(str(d), "{1 : one, 2 : two, 3 : three}")

    def test_get(self):
        d = MyDict()
        d.set(1, "one")
        d.set(2, "two")
        d.set(3, "three")

        self.assertEqual(d.get(1), "one")
        self.assertEqual(d.get(2), "two")
        self.assertEqual(d.get(3), "three")
        self.assertIsNone(d.get(4))

    def test_popitem(self):
        d = MyDict()

        d.set(1, "one")
        d.set(2, "two")

        self.assertEqual(len(d), 2)

        a = d.popitem()
        a_key = a[0]

        self.assertEqual(a, (1, "one"))
        self.assertFalse(a_key in d)
        self.assertEqual(len(d), 1)

        b = d.popitem()
        b_key = b[0]
        self.assertEqual(b, (2, "two"))
        self.assertFalse(b_key in d)
        self.assertEqual(len(d), 0)

        with self.assertRaises(KeyError):
            d.popitem()

    def test_len(self):
        d = MyDict()
        self.assertEqual(len(d), 0)

        d.set(1, "one")
        d.set(2, "two")
        d.set(3, "three")

        self.assertEqual(len(d), 3)

    def test_contains(self):
        d = MyDict()

        self.assertFalse(1 in d)
        d.set(1, "one")
        self.assertTrue(1 in d)

    def test_str(self):
        d = MyDict()

        self.assertEqual(str(d), "{}")

        d.set(1, "one")
        d.set(2, "two")

        self.assertEqual(str(d), "{1 : one, 2 : two}")

    def test_clear(self):
        d = MyDict()

        d.set(1, "one")
        d.set(2, "two")

        self.assertEqual(str(d), "{1 : one, 2 : two}")

        d.clear()
        self.assertEqual(str(d), "{}")


if __name__ == "__main__":
    unittest.main()