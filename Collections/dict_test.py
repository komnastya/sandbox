import unittest

from dict import MyDict


class TestMyDict(unittest.TestCase):
    def test_dict(self):
        d = MyDict()

        self.assertEqual(len(d), 0)
        self.assertEqual(str(d), "{}")
        self.assertFalse(1 in d)
        self.assertIsNone(d.get(1))

        d.set(1, "one")

        self.assertEqual(len(d), 1)
        self.assertEqual(str(d), "{1: one}")
        self.assertTrue(1 in d)
        self.assertEqual(d.get(1), "one")

        d.set(1, "uno")

        self.assertEqual(len(d), 1)
        self.assertEqual(str(d), "{1: uno}")
        self.assertTrue(1 in d)
        self.assertEqual(d.get(1), "uno")

        d.set(3, "tre")
        d.set(2, "due")

        self.assertEqual(len(d), 3)
        self.assertEqual(str(d), "{1: uno, 2: due, 3: tre}")
        self.assertTrue(1 in d)
        self.assertEqual(d.get(1), "uno")
        self.assertTrue(2 in d)
        self.assertEqual(d.get(2), "due")
        self.assertTrue(3 in d)
        self.assertEqual(d.get(3), "tre")

    def test_get(self):
        d = MyDict()
        d.set(1, "one")
        d.set(2, "two")
        d.set(3, "three")

        self.assertEqual(d.get(1), "one")
        self.assertEqual(d.get(2), "two")
        self.assertEqual(d.get(3), "three")
        self.assertIsNone(d.get(4))

    def test_getitem(self):
        d = MyDict()

        with self.assertRaises(KeyError):
            d[1]

        d.set(1, "one")
        d.set(2, "two")
        d.set(3, "three")

        self.assertEqual(d[1], "one")
        self.assertEqual(d[2], "two")
        self.assertEqual(d[3], "three")

    def test_setitem(self):
        d = MyDict()

        self.assertEqual(len(d), 0)
        self.assertEqual(str(d), "{}")
        self.assertFalse(1 in d)
        self.assertIsNone(d.get(1))

        d[1] = "one"
        d[2] = "two"

        self.assertEqual(len(d), 2)
        self.assertEqual(str(d), "{1: one, 2: two}")
        self.assertTrue(1 in d)
        self.assertTrue(2 in d)
        self.assertEqual(d.get(1), "one")
        self.assertEqual(d.get(2), "two")

    def test_delitem(self):
        d = MyDict()

        self.assertEqual(len(d), 0)
        self.assertEqual(str(d), "{}")
        self.assertFalse(1 in d)
        self.assertIsNone(d.get(1))

        d[1] = "one"
        d[2] = "two"

        self.assertEqual(len(d), 2)
        self.assertEqual(str(d), "{1: one, 2: two}")

        del d[1]
        del d[2]

        self.assertEqual(len(d), 0)
        self.assertEqual(str(d), "{}")

        with self.assertRaises(KeyError):
            del d[1]

    def test_pop(self):
        d = MyDict()

        d[1] = "one"

        self.assertEqual(d.pop(1), "one")

        with self.assertRaises(KeyError):
            d.pop(2)

        self.assertEqual(d.pop(3, "Not found"), "Not found")

    def test_setdefault(self):
        d = MyDict()

        d[1] = "one"

        self.assertEqual(d.setdefault(1), "one")
        self.assertEqual(d.setdefault(1, "uno"), "one")
        self.assertIsNone(d.setdefault(2))
        self.assertEqual(d.setdefault(2, "two"), "two")

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
        d[1] = "one"
        self.assertTrue(1 in d)

        d_items = d.items()
        self.assertTrue(1 in d_items)
        self.assertFalse("one" in d_items)

        d_keys = d.keys()
        self.assertTrue(1 in d_keys)
        self.assertFalse("one" in d_keys)

        d_values = d.values()
        self.assertTrue("one" in d_values)
        self.assertFalse(1 in d_values)

    def test_str(self):
        d = MyDict()

        self.assertEqual(str(d), "{}")

        d.set(1, "one")
        d.set(2, "two")

        self.assertEqual(str(d), "{1: one, 2: two}")

    def test_clear(self):
        d = MyDict()

        d.set(1, "one")
        d.set(2, "two")

        self.assertEqual(str(d), "{1: one, 2: two}")

        d.clear()
        self.assertEqual(str(d), "{}")

    def test_copy(self):
        d = MyDict()

        d.set(1, "one")
        d.set(2, "two")
        self.assertEqual(str(d), "{1: one, 2: two}")

        dd = d.copy()
        del d[2]
        dd[3] = "three"
        self.assertEqual(str(d), "{1: one}")
        self.assertEqual(str(dd), "{1: one, 2: two, 3: three}")

    def test_fromkeys(self):
        self.assertEqual(
            str(MyDict().fromkeys([1, 2, 3])), "{1: None, 2: None, 3: None}"
        )
        self.assertEqual(
            str(MyDict().fromkeys([1, 2, 3], "number")),
            "{1: number, 2: number, 3: number}",
        )

    def test_dictitems(self):
        d = MyDict()
        self.assertEqual(str(d.items()), "dict_items[]")

        d[1] = "one"
        d[2] = "two"

        self.assertEqual(str(d.items()), "dict_items[(1, one), (2, two)]")
        self.assertEqual(len(d.items()), 2)

    def test_dictkeys(self):
        d = MyDict()
        self.assertEqual(str(d.keys()), "dict_keys[]")

        d[1] = "one"
        d[2] = "two"

        self.assertEqual(str(d.keys()), "dict_keys[1, 2]")
        self.assertEqual(len(d.keys()), 2)

    def test_dictvalues(self):
        d = MyDict()
        self.assertEqual(str(d.values()), "dict_values[]")

        d[1] = "one"
        d[2] = "two"

        self.assertEqual(str(d.values()), "dict_values[one, two]")
        self.assertEqual(len(d.values()), 2)

    def test_documentation(self):
        d = MyDict()

        self.assertEqual(d.__doc__, "My own dictionary class")

        items = d.items()
        self.assertEqual(items.__doc__, "My class for dictionary items")

        keys = d.keys()
        self.assertEqual(keys.__doc__, "My class for dictionary keys")

        values = d.values()
        self.assertEqual(values.__doc__, "My class for dictionary values")

    def test_eq(self):
        d = MyDict()
        dd = d
        c = MyDict()

        self.assertEqual(d, dd)
        self.assertEqual(c, d)
        self.assertEqual(c, dd)

        self.assertIs(d, dd)
        self.assertIsNot(c, d)
        self.assertIsNot(c, dd)

        d[1] = 'one'
        dd[2] = 'two'
        c[3] = 'three'

        self.assertEqual(d, dd)
        self.assertIs(d, dd)
        self.assertNotEqual(c, d)
        self.assertNotEqual(c, dd)

        c[3] = 'one'
        c[4] = 'two'

        self.assertIsNot(c, d)
        self.assertNotEqual(c, d)
        self.assertIsNot(c, dd)
        self.assertNotEqual(c, dd)
        self.assertIs(d, dd)
        self.assertEqual(d, dd)

    def test_update(self):
        d = MyDict()
        d[1] = 'one'
        d[2] = 'three'

        d1 = MyDict()
        d1[2] = 'two'
        self.assertEqual(str(d), '{1: one, 2: three}')

        d.update(d1)
        self.assertEqual(str(d), '{1: one, 2: two}')

        d1[3] = 'three'
        d.update(d1)
        self.assertEqual(str(d), '{1: one, 2: two, 3: three}')


if __name__ == "__main__":
    unittest.main()
