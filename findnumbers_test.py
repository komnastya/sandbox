from findnumbers import (
    find_numbers,
    find_numbers_2,
    find_numbers_sm,
)


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
    nums = find_numbers_2("")
    assert list(nums) == []

    nums = find_numbers_2("no numbers here")
    assert list(nums) == []

    nums = find_numbers_2("0")
    assert list(nums) == [0]

    nums = find_numbers_2("012")
    assert list(nums) == [12]

    nums = find_numbers_2("0 1 2")
    assert list(nums) == [0, 1, 2]

    nums = find_numbers_2("0, 1, 2,")
    assert list(nums) == [0, 1, 2]

    nums = find_numbers_2("(123)")
    assert list(nums) == [123]

    nums = find_numbers_2('2some34numbers56here78"')
    assert list(nums) == [2, 34, 56, 78]

    nums = find_numbers_2("-1+2")
    assert list(nums) == [1, 2]


def test_find_numbers_sm():
    nums = find_numbers_sm("")
    assert list(nums) == []

    nums = find_numbers_sm("no numbers here")
    assert list(nums) == []

    nums = find_numbers_sm("0")
    assert list(nums) == [0]

    nums = find_numbers_sm("012")
    assert list(nums) == [12]

    nums = find_numbers_sm("0 1 2")
    assert list(nums) == [0, 1, 2]

    nums = find_numbers_sm("0, 1, 2,")
    assert list(nums) == [0, 1, 2]

    nums = find_numbers_sm("(123)")
    assert list(nums) == [123]

    nums = find_numbers_sm('2some34numbers56here78"')
    assert list(nums) == [2, 34, 56, 78]

    nums = find_numbers_sm("-1+2")
    assert list(nums) == [1, 2]
