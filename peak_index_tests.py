import unittest
from peak_index import peak_index

class TestPeakIndex(unittest.TestCase):
  def test_peak_index(self):
    self.assertEqual(peak_index([0,1,0]), 1)
    self.assertEqual(peak_index([1,3,5,7,9,11,6,3]), 5)

if __name__ == '__main__':
  unittest.main()
