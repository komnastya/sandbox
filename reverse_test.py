from reverse import reverse


def test_reverse():
    assert reverse([]) == []
    assert reverse([1]) == [1]
    assert reverse([1, 2]) == [2, 1]
    assert reverse([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
