from sorting import (
    bubble_sort,
    insert_sort,
    merge_sort,
    merge_sort_2,
    quick_sort,
    select_sort,
)


def _check_sorting_function(sf):
    assert sf([]) == []
    assert sf([1]) == [1]
    assert sf([1, 2]) == [1, 2]
    assert sf([2, 1]) == [1, 2]
    assert sf([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]


def test_bubble_sort():
    _check_sorting_function(bubble_sort)


def test_select_sort():
    _check_sorting_function(select_sort)


def test_insert_sort():
    _check_sorting_function(insert_sort)


def test_quick_sort():
    _check_sorting_function(quick_sort)


def test_merge_sort():
    _check_sorting_function(merge_sort)


def test_merge_sort_2():
    _check_sorting_function(merge_sort_2)
