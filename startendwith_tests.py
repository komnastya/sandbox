from startendwith import ends_with, starts_with


def test_starts_with():
    assert starts_with([1, 2, 3], []) == True
    assert starts_with([1, 2, 3], [1]) == True
    assert starts_with([1, 2, 3], [1, 2]) == True
    assert starts_with([1, 2, 3], [1, 2, 3]) == True
    assert starts_with([1, 2, 3], [2]) == False
    assert starts_with([1, 2, 3], [1, 2, 3, 4]) == False


def tests_ends_with():
    assert ends_with([1, 2, 3], []) == True
    assert ends_with([1, 2, 3], [3]) == True
    assert ends_with([1, 2, 3], [2, 3]) == True
    assert ends_with([1, 2, 3], [1, 2, 3]) == True
    assert ends_with([1, 2, 3], [2]) == False
    assert ends_with([1, 2, 3], [1, 2, 3, 4]) == False
