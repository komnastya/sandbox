# python -m unittest discover -p "*_test.py"
import pytest

from shift import (
    shift_for,
    shift_inplace_smart,
    shift_inplace_stupid,
    shift_reverse,
    shift_slices,
    shift_while,
)


def test_shift_reverse():
    assert shift_reverse([]) == []
    assert shift_reverse([1]), [1]
    assert shift_reverse([1, 2, 3, 4, 5]) == [5, 1, 2, 3, 4]


def test_shift_while():
    assert shift_while([]) == []
    assert shift_while([1]) == [1]
    assert shift_while([1, 2, 3, 4, 5]) == [2, 3, 4, 5, 1]


def test_shift_for():
    assert shift_for([]) == []
    assert shift_for([1]), [1]
    assert shift_for([1, 2, 3, 4, 5]) == [2, 3, 4, 5, 1]


def test_shift_slices():
    assert shift_slices([]) == []
    assert shift_slices([1]) == [1]
    assert shift_slices([1, 2, 3, 4, 5]) == [2, 3, 4, 5, 1]


def test_shift_inplace_smart():
    list = []
    shift_inplace_smart(list)
    assert list == []

    list = [1]
    shift_inplace_smart(list)
    assert list == [1]

    list = [1, 2, 3, 4, 5]
    shift_inplace_smart(list)
    assert list == [2, 3, 4, 5, 1]


def test_shift_inplace_stupid():
    list = [1, 2, 3, 4, 5]
    shift_inplace_stupid(list)
    assert list == [2, 3, 4, 5, 1]

    list = []
    with pytest.raises(ValueError):
        shift_inplace_stupid(list)

    list = [1]
    with pytest.raises(ValueError):
        shift_inplace_stupid(list)
