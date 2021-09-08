import pytest

from combine import combine, my_combine


def test_exception():
    with pytest.raises(ValueError):
        my_combine([1], [1, 2])
    with pytest.raises(ValueError):
        combine([1], [1, 2])


def test_my_combine():
    assert my_combine([], []) == []
    assert my_combine([1], [1]) == [1, 1]
    assert my_combine([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]


def test_combine():
    assert combine([], []) == []
    assert combine([1], [1]) == [(1, 1)]
    assert combine([1, 3, 5], [2, 4, 6]) == [(1, 2), (3, 4), (5, 6)]
