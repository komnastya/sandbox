from merge_lists import merge_lists


def test_merge():
    assert merge_lists([], []) == []
    assert merge_lists([1, 1, 1], []) == [1, 1, 1]
    assert merge_lists([], [2, 2, 2]) == [2, 2, 2]
    assert merge_lists([2, 4, 6], [1, 3, 5]) == [1, 2, 3, 4, 5, 6]
    assert merge_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_lists([1, 1, 1], [2, 2, 2]) == [1, 1, 1, 2, 2, 2]
    assert merge_lists([2, 2, 2], [1, 1, 1]) == [1, 1, 1, 2, 2, 2]
