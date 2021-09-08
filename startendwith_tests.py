from startendwith import ends_with, starts_with


def test_starts_with():
    assert starts_with([1, 2, 3], [])
    assert starts_with([1, 2, 3], [1])
    assert starts_with([1, 2, 3], [1, 2])
    assert starts_with([1, 2, 3], [1, 2, 3])
    assert not starts_with([1, 2, 3], [2])
    assert not starts_with([1, 2, 3], [1, 2, 3, 4])


def tests_ends_with():
    assert ends_with([1, 2, 3], [])
    assert ends_with([1, 2, 3], [3])
    assert ends_with([1, 2, 3], [2, 3])
    assert ends_with([1, 2, 3], [1, 2, 3])
    assert not ends_with([1, 2, 3], [2])
    assert not ends_with([1, 2, 3], [1, 2, 3, 4])
