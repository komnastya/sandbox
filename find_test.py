from find import find


def test_find():
    assert find([], 1) == -1
    assert find([1, 1, 1, 1, 1], 1) == 0
    assert find([1, 2, 3, 4, 5], 1) == 0
    assert find([1, 2, 3, 4, 5], 3) == 2
    assert find([1, 2, 3, 4, 5], 5) == 4
    assert find([1, 2, 3, 4, 5], 0) == -1
