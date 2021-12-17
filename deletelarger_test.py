from deletelarger import (
    delete_large,
    delete_large_fast,
    delete_large_slow,
    delete_small,
)


def test_delete_large():
    assert delete_large([1, 2, 3, 4, 5, 6, 7, 8, 1], 1) == [1, 1]
    assert delete_large([1, 2, 3, 4, 5, 6, 7, 8, 1], 3) == [1, 2, 3, 1]
    assert delete_large([1, 2, 3, 4, 5, 6, 7, 8, 9], 9) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_delete_large_slow():
    list = [1, 11, 2, 12, 3, 13, 4, 14, 5, 15]
    delete_large_slow(list, 10)
    assert list == [1, 2, 3, 4, 5]

    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    delete_large_slow(list, 5)
    assert list == [1, 2, 3, 4, 5]


def test_delete_small():
    list = [1, 11, 2, 12, 3, 13, 4, 14, 5, 15]
    delete_small(list, 10)
    assert list == [11, 12, 13, 14, 15]

    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    delete_small(list, 5)
    assert list == [6, 7, 8, 9, 10]


def test_delete_large_fast():
    list = [1, 11, 2, 12, 3, 13, 4, 14, 5, 15]
    delete_large_fast(list, 10)
    assert list == [1, 2, 3, 4, 5]

    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    delete_large_fast(list, 5)
    assert list == [1, 2, 3, 4]
