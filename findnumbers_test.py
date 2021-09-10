import pytest

from findnumbers import find_numbers, find_numbers_2


def test_findnumbers():
    assert find_numbers("") == []
    assert find_numbers("no numbers here") == []
    assert find_numbers("0") == [0]
    assert find_numbers("012") == [12]
    assert find_numbers("0 1 2") == [0, 1, 2]
    assert find_numbers("0,1,2,") == [0, 1, 2]
    assert find_numbers("(123)") == [123]
    assert find_numbers("12some34numbers56here78") == [12, 34, 56, 78]
    assert find_numbers("-1+2") == [1, 2]


def test_find_numbers2():
    nums = find_numbers_2('')
    with pytest.raises(StopIteration):
        next(nums)

    nums = find_numbers_2('no numbers here')
    with pytest.raises(StopIteration):
        next(nums)

    nums = find_numbers_2('0')
    assert next(nums) == 0

    nums = find_numbers_2('012')
    assert next(nums) == 12

    nums = find_numbers_2('0 1 2')
    assert next(nums) == 0
    assert next(nums) == 1
    assert next(nums) == 2

    nums = find_numbers_2('0, 1, 2,')
    assert next(nums) == 0
    assert next(nums) == 1
    assert next(nums) == 2

    nums = find_numbers_2('(123)')
    assert next(nums) == 123

    nums = find_numbers_2('2some34numbers56here78"')
    assert next(nums) == 2
    assert next(nums) == 34
    assert next(nums) == 56
    assert next(nums) == 78

    nums = find_numbers_2('-1+2')
    assert next(nums) == 1
    assert next(nums) == 2
