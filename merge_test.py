from merge import merge, merge_better, merge_ugly


def test_merge():
    assert list(merge([], [])) == []
    assert list(merge([1, 1, 1], [])) == [1, 1, 1]
    assert list(merge([], [2, 2, 2])) == [2, 2, 2]
    assert list(merge([2, 4, 6], [1, 3, 5])) == [1, 2, 3, 4, 5, 6]
    assert list(merge([1, 3, 5], [2, 4, 6])) == [1, 2, 3, 4, 5, 6]
    assert list(merge([1, 1, 1], [2, 2, 2])) == [1, 1, 1, 2, 2, 2]
    assert list(merge([2, 2, 2], [1, 1, 1])) == [1, 1, 1, 2, 2, 2]


def test_merge_better():
    assert list(merge_better([], [])) == []
    assert list(merge_better([1, 1, 1], [])) == [1, 1, 1]
    assert list(merge_better([], [2, 2, 2])) == [2, 2, 2]
    assert list(merge_better([2, 4, 6], [1, 3, 5])) == [1, 2, 3, 4, 5, 6]
    assert list(merge_better([1, 3, 5], [2, 4, 6])) == [1, 2, 3, 4, 5, 6]
    assert list(merge_better([1, 1, 1], [2, 2, 2])) == [1, 1, 1, 2, 2, 2]
    assert list(merge_better([2, 2, 2], [1, 1, 1])) == [1, 1, 1, 2, 2, 2]


def test_merge_ugly():
    assert list(merge_ugly([], [])) == []
    assert list(merge_ugly([1, 1, 1], [])) == [1, 1, 1]
    assert list(merge_ugly([], [2, 2, 2])) == [2, 2, 2]
    assert list(merge_ugly([2, 4, 6], [1, 3, 5])) == [1, 2, 3, 4, 5, 6]
    assert list(merge_ugly([1, 3, 5], [2, 4, 6])) == [1, 2, 3, 4, 5, 6]
    assert list(merge_ugly([1, 1, 1], [2, 2, 2])) == [1, 1, 1, 2, 2, 2]
    assert list(merge_ugly([2, 2, 2], [1, 1, 1])) == [1, 1, 1, 2, 2, 2]
