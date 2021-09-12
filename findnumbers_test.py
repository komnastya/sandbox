from findnumbers import (
    find_numbers,
    find_numbers_2,
    find_numbers_sm,
    find_numbers_sm_bool,
)


def test_findnumbers():
    run_test_cases(find_numbers)


def test_find_numbers2():
    run_test_cases(find_numbers_2)


def test_find_numbers_sm_bool():
    run_test_cases(find_numbers_sm_bool)


def test_find_numbers_sm():
    run_test_cases(find_numbers_sm)


def run_test_cases(func):
    assert list(func("")) == []
    assert list(func("no numbers here")) == []
    assert list(func("0")) == [0]
    assert list(func("012")) == [12]
    assert list(func("0 1 2")) == [0, 1, 2]
    assert list(func("0,1,2,")) == [0, 1, 2]
    assert list(func("(123)")) == [123]
    assert list(func("12some34numbers56here78")) == [12, 34, 56, 78]
    assert list(func("-1+2")) == [1, 2]
