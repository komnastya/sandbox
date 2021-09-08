from myiterators import even, head, odd, skip


def test_head():
    assert list(head([], 10)) == []
    assert list(head([1, 2, 3], 10)) == [1, 2, 3]
    assert list(head([1, 2, 3], 0)) == []
    assert list(head([1, 2, 3, 4, 5, 6, 7, 8], 5)) == [1, 2, 3, 4, 5]


def test_skip():
    assert list(skip([], 10)) == []
    assert list(skip([1, 2, 3], 10)) == []
    assert list(skip([1, 2, 3], 0)) == [1, 2, 3]
    assert list(skip([1, 2, 3, 4, 5], 3)) == [4, 5]


def test_even():
    assert list(even([])) == []
    assert list(even([1, 2, 3, 4])) == [1, 3]


def test_odd():
    assert list(odd([])) == []
    assert list(odd([1, 2, 3, 4])) == [2, 4]


def test_head_skip_odd_even_together():
    assert list(even(head([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6))) == [0, 2, 4]
    assert list(odd(head([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6))) == [1, 3, 5]
    assert list(even(skip([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))) == [5, 7, 9]
    assert list(odd(skip([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))) == [6, 8, 10]
    assert list(head(odd([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3)) == [1, 3, 5]
    assert list(head(even([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3)) == [0, 2, 4]
    assert list(skip(odd([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3)) == [7, 9]
    assert list(skip(even([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3)) == [6, 8, 10]
