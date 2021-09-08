import pytest

from has_next_iterator import HasNextIterator


def test_has_next_iterator():
    nums = HasNextIterator(iter([1, 2, 3, 4, 5]))
    assert list(nums) == [1, 2, 3, 4, 5]


def test_has_next_method():
    nums_1 = HasNextIterator(iter([]))
    assert not nums_1.has_next()

    nums = HasNextIterator(iter([1, 2, 3]))
    assert nums.has_next()
    assert next(nums) == 1

    assert nums.has_next()
    assert next(nums) == 2

    assert nums.has_next()
    assert next(nums) == 3

    assert not nums.has_next()
    assert not nums.has_next()


def test_next_method_exception():
    nums = HasNextIterator(iter([1, 2, 3]))

    next(nums)
    next(nums)
    next(nums)

    with pytest.raises(StopIteration):
        next(nums)
