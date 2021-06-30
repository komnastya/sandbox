import unittest
from classnumberset import NumberSet


class TestNumberSetCalss(unittest.TestCase):
    def test_insert(self):
        s = NumberSet()
        self.assertEqual(list(s), [])
        s.insert(1)
        s.insert(11)
        self.assertEqual(sorted(list(s)), [1, 11])

    def test_insert_duplicates(self):
        s = NumberSet()
        self.assertEqual(list(s), [])
        s.insert(1)
        s.insert(1)
        s.insert(1)
        self.assertEqual(sorted(list(s)), [1])

    def test_delete(self):
        s = NumberSet()
        self.assertFalse(s.has(1))
        s.delete(1)
        self.assertFalse(s.has(1))
        s.insert(1)
        self.assertTrue(s.has(1))
        s.delete(1)
        self.assertFalse(s.has(1))

    def test_has(self):
        s = NumberSet()
        self.assertFalse(s.has(1))
        s.insert(1)
        self.assertTrue(s.has(1))

    def test_iterator(self):
        s = NumberSet()
        s.insert(1)
        s.insert(2)
        s.insert(3)
        self.assertEqual(sorted(list(s)), [1, 2, 3])

    def test_len(self):
        s = NumberSet()
        self.assertEqual(len(s), 0)
        s.insert(1)
        s.insert(2)
        s.insert(3)
        self.assertEqual(len(s), 3)
        s.delete(3)
        self.assertEqual(len(s), 2)

    def test_str(self):
        s = NumberSet()
        self.assertEqual(str(s), "{}")
        s.insert(1)
        s.insert(2)
        s.insert(3)

        self.assertEqual(str(s), "{1, 2, 3}")


if __name__ == "__main__":
    unittest.main(exit=False)
