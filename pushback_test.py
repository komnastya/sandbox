import pytest

from pushback import PushBackIterator


def test_push_back_iterator():
    nums = PushBackIterator(iter([1, 2, 3, 4, 5]))
    assert list(nums) == [1, 2, 3, 4, 5]


def test_push_back_method():
    nums = PushBackIterator(iter([3, 4, 5]))
    assert next(nums) == 3

    nums.push_back(3)
    assert next(nums) == 3

    nums.push_back(3)
    nums.push_back(2)
    nums.push_back(1)
    assert list(nums) == [1, 2, 3, 4, 5]


def test_has_next_method():
    nums = PushBackIterator(iter([]))
    assert not nums.has_next()

    nums = PushBackIterator(iter([1, 2, 3]))
    assert next(nums) == 1

    assert nums.has_next()
    assert next(nums) == 2

    assert nums.has_next()
    assert next(nums) == 3

    assert not nums.has_next()


def test_has_next_and_push_back_methods_together():
    nums = PushBackIterator(iter([3, 4]))

    assert next(nums) == 3
    assert next(nums) == 4

    assert not nums.has_next()

    nums.push_back(5)
    assert nums.has_next()

    assert next(nums) == 5
    assert not nums.has_next()

    nums = PushBackIterator(iter([]))
    assert not nums.has_next()
    nums.push_back(1)
    assert list(nums) == [1]


def test_exceptions():
    nums = PushBackIterator(iter([1, 2, 3]))

    next(nums)
    next(nums)
    next(nums)

    with pytest.raises(StopIteration):
        next(nums)


def test_exception_with_push():
    nums = PushBackIterator(iter([1, 2]))
    next(nums)
    next(nums)

    nums.push_back(1)
    nums.push_back(2)

    next(nums)
    next(nums)

    with pytest.raises(StopIteration):
        next(nums)
