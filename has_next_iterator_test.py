import pytest

from has_next_iterator import HasNextIterator


def test_has_next_iterator():
    nums = HasNextIterator(iter([1, 2, 3, 4, 5]))
    assert list(nums) == [1, 2, 3, 4, 5]


def test_has_next_method():
    nums_1 = HasNextIterator(iter([]))
    assert nums_1.has_next() == False

    nums = HasNextIterator(iter([1, 2, 3]))
    assert nums.has_next() == True
    assert next(nums) == 1

    assert nums.has_next() == True
    assert next(nums) == 2

    assert nums.has_next() == True
    assert next(nums) == 3

    assert nums.has_next() == False
    assert nums.has_next() == False


def test_next_method_exception():
    nums = HasNextIterator(iter([1, 2, 3]))

    next(nums)
    next(nums)
    next(nums)

    with pytest.raises(StopIteration):
        next(nums)
