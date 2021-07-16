import pytest
from sorting import bubble_sort, select_sort


def test_sorting():
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]
    assert bubble_sort([1, 2]) == [1, 2]
    assert bubble_sort([2, 1]) == [1, 2]
    assert bubble_sort([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]


def test_sorting2():
    assert select_sort([]) == []
    assert select_sort([1]) == [1]
    assert select_sort([1, 2]) == [1, 2]
    assert select_sort([2, 1]) == [1, 2]
    assert select_sort([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]
