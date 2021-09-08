import pytest

from ranges import MyRange, my_range


def test_myrange_class_initialization():
    nums = MyRange(1, 6)
    assert list(nums) == [1, 2, 3, 4, 5]

    nums = MyRange(1, 1)
    assert list(nums) == []


def test_next_method():
    nums = MyRange(1, 4)

    next(nums)
    next(nums)
    next(nums)

    with pytest.raises(StopIteration):
        next(nums)


def test_my_range_function():
    assert list(my_range(1, 4)) == [1, 2, 3]
    assert list(my_range(4, 1)) == []
