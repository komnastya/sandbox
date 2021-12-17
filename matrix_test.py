import pytest

from matrix import is_square, matrix_sum


def test_matrix():
    assert is_square([[1, 2], [3, 4]])
    assert is_square([])
    assert is_square([[1]])
    with pytest.raises(ValueError):
        matrix_sum([[1, 2], [3, 4]], [[1, 2]])


def test_matrix_sum():
    assert matrix_sum([], []) == []
    assert matrix_sum([[1, 2], [3, 4]], [[5, 6], [7, 8]]) == [[6, 8], [10, 12]]

    with pytest.raises(ValueError):
        matrix_sum([[1, 2], [3, 4]], [[1, 2]])
