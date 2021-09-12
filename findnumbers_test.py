from findnumbers import (
    find_numbers,
    find_numbers_2,
    find_numbers_sm,
    find_numbers_sm_bool,
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
    run_test_cases(find_numbers_2)


def test_find_numbers_sm_bool():
    run_test_cases(find_numbers_sm_bool)


def test_find_numbers_sm():
    run_test_cases(find_numbers_sm)


def run_test_cases(func):
    nums = func("")
    assert list(nums) == []

    nums = func("no numbers here")
    assert list(nums) == []

    nums = func("0")
    assert list(nums) == [0]

    nums = func("012")
    assert list(nums) == [12]

    nums = func("0 1 2")
    assert list(nums) == [0, 1, 2]

    nums = func("0, 1, 2,")
    assert list(nums) == [0, 1, 2]

    nums = func("(123)")
    assert list(nums) == [123]

    nums = func('2some34numbers56here78"')
    assert list(nums) == [2, 34, 56, 78]

    nums = func("-1+2")
    assert list(nums) == [1, 2]
