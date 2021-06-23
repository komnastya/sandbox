import unittest
from sumoddlenghtsubarrays import sumOddLengthSubarrays

class TestSumOddLengthSubarrays (unittest.TestCase):
  def test_sumoddlengthsubarrays(self):
    self.assertEqual(sumOddLengthSubarrays([]), 0)
    self.assertEqual(sumOddLengthSubarrays([1]), 1)
    self.assertEqual(sumOddLengthSubarrays([1,2]), 3)
    self.assertEqual(sumOddLengthSubarrays([1,2,3]), 12)
    self.assertEqual(sumOddLengthSubarrays([1,2,3,4]), 25)
    self.assertEqual(sumOddLengthSubarrays([-1,-2,-3,-4]), -25)



if __name__ == "__main__":
  unittest.main()
