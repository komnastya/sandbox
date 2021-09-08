from non_repeating import non_repeating_better, non_repeating_one, non_repeating_two


def test_non_repeating_one():
    assert list(non_repeating_one([])) == []
    assert list(non_repeating_one([1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]
    assert list(non_repeating_one([1, 2, 1, 2, 1])) == [1, 2, 1, 2, 1]
    assert list(non_repeating_one([1, 1, 1, 1, 1])) == [1]
    assert list(non_repeating_one([1, 1, 2, 2, 2])), [1, 2]
    assert list(non_repeating_one([1, 2, 2, 3, 4, 4, 5, 6, 6])), [1, 2, 3, 4, 5, 6]


def test_non_repeating_two():
    assert list(non_repeating_two([])) == []
    assert list(non_repeating_two([1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]
    assert list(non_repeating_two([1, 2, 1, 2, 1])) == [1, 2, 1, 2, 1]
    assert list(non_repeating_two([1, 1, 1, 1, 1])) == [1]
    assert list(non_repeating_two([1, 1, 2, 2, 2])), [1, 2]
    assert list(non_repeating_two([1, 2, 2, 3, 4, 4, 5, 6, 6])) == [1, 2, 3, 4, 5, 6]


def test_non_repeating_better():
    assert list(non_repeating_better([])) == []
    assert list(non_repeating_better([None, None, None])) == [None]
    assert list(non_repeating_better([1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]
    assert list(non_repeating_better([1, 2, 1, 2, 1])) == [1, 2, 1, 2, 1]
    assert list(non_repeating_better([1, 1, 1, 1, 1])) == [1]
    assert list(non_repeating_better([1, 1, 2, 2, 2])) == [1, 2]
    assert list(non_repeating_better([1, 2, 2, 3, 4, 4, 5, 6, 6])) == [1, 2, 3, 4, 5, 6]
    assert list(non_repeating_better([None, None, None])) == [None]
    assert list(non_repeating_better([True, True, True])) == [True]
    assert list(non_repeating_better([True, True, False, False, True, False])) == [True, False, True, False]
