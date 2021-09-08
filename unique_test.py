from unique import unique


def test_unique():
    assert list(unique([])) == []
    assert list(unique([1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]
    assert list(unique([1, 2, 1, 2, 1])) == [1, 2]
    assert list(unique([1, 1, 1, 1, 1])) == [1]
    assert list(unique([1, 1, 2, 2, 2])) == [1, 2]
