import pytest
from intersection import intersect


def test_intersection():
    assert intersect([], []) == []
    assert intersect([1, 2, 3], []) == []
    assert intersect([1, 2, 3], [4, 5, 6]) == []
    assert intersect([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]) == [4, 5]
    assert intersect([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert intersect([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7, 8]) == [1, 2, 3, 4, 5]
