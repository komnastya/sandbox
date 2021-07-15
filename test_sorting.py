import pytest
from sorting import sorting, sorting2

def test_sorting():
  assert sorting([]) == []
  assert sorting([1]) == [1]
  assert sorting([1,2]) == [1,2]
  assert sorting([2,1]) == [1,2]
  assert sorting([5,3,1,4,2]) == [1,2,3,4,5]

def test_sorting2():
  assert sorting2([]) == []
  assert sorting2([1]) == [1]
  assert sorting2([1,2]) == [1,2]
  assert sorting2([2,1]) == [1,2]
  assert sorting2([5,3,1,4,2]) == [1,2,3,4,5]
