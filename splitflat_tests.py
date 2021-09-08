from splitflat import equal, flat, split


def test_equal():
    assert equal([], []) == True
    assert equal([1], [1]) == True
    assert equal([1, 2], [1, 2]) == True
    assert equal([1, 2, 3], [1, 2]) == False
    assert equal([1, 2], [2, 1]) == False


def test_flat():
    assert flat([]) == []
    assert flat([[1], [2]]) == [1, 2]
    assert flat([[1, 2, 3], [4, 5, 6]]) == [1, 2, 3, 4, 5, 6]
    assert flat([[1], [2], [3], [4, 5], [6]]) == [1, 2, 3, 4, 5, 6]


def test_flat_2():
    assert flat([]) == []
    assert flat([[1], [2]]) == [1, 2]
    assert flat([[1, 2, 3], [4, 5, 6]]) == [1, 2, 3, 4, 5, 6]
    assert flat([[1], [2], [3], [4, 5], [6]]) == [1, 2, 3, 4, 5, 6]


def test_split():
    assert split([1, 2, 3], 1) == [[1], [2], [3]]
    assert split([1, 2, 3], 2) == [[1, 2], [3]]
    assert split([1, 2, 3], 10) == [[1, 2, 3]]
    assert split([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
