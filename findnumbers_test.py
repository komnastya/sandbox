import pytest

from findnumbers import find_numbers, find_numbers_2


def test_findnumbers():
    run_test_cases(find_numbers)


def test_find_numbers_2():
    run_test_cases(find_numbers_2)


def run_test_cases(func):
    assert func("") == []
    assert func("no numbers here") == []
    assert func("0") == [0]
    assert func("012") == [12]
    assert func("0 1 2") == [0, 1, 2]
    assert func("0,1,2,") == [0, 1, 2]
    assert func("(123)") == [123]
    assert func("12some34numbers56here78") == [12, 34, 56, 78]
    assert func("-1+2") == [1, 2]
