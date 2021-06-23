import unittest
from majority_element import majority_element_for, majority_element_while


class TestMajorElement(unittest.TestCase):
    def test_majority_element_for(self):
        self.assertIsNone(majority_element_for([]))
        self.assertEqual(majority_element_for([1]), 1)
        self.assertEqual(majority_element_for([1, 1, 1]), 1)
        self.assertEqual(majority_element_for([3, 2, 3]), 3)
        self.assertEqual(majority_element_for([2, 2, 1, 1, 1, 2, 2]), 2)

    def test_majority_element_while(self):
        self.assertIsNone(majority_element_while([]))
        self.assertEqual(majority_element_while([1]), 1)
        self.assertEqual(majority_element_while([1, 1, 1]), 1)
        self.assertEqual(majority_element_while([3, 2, 3]), 3)
        self.assertEqual(majority_element_while([2, 2, 1, 1, 1, 2, 2]), 2)


if __name__ == "__main__":
    unittest.main()
