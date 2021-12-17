from sort import is_sorted


def test_is_sorted():
    assert is_sorted([])
    assert is_sorted([1])
    assert is_sorted([1, 2])
    assert not is_sorted([3, 2, 1])
