from sort import is_sorted


def test_is_sorted():
    assert is_sorted([]) == False
    assert is_sorted([1]) == True
    assert is_sorted([1, 2]) == True
    assert is_sorted([3, 2, 1]) == False
