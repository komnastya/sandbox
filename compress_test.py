import pytest

from compress import compress, decompress, element_by_index, element_by_index2


def test_decompress():
    assert decompress([]) == []
    assert decompress([(1, 3)]) == [1, 1, 1]
    assert decompress([(1, 1), (2, 1), (3, 1)]) == [1, 2, 3]
    assert decompress([(1, 3), (2, 5)]) == [1, 1, 1, 2, 2, 2, 2, 2]
    assert decompress([(999, 0)]) == []


def test_compress():
    assert compress([]) == []
    assert compress([1, 1, 1]) == [(1, 3)]
    assert compress([1, 2, 3]) == [(1, 1), (2, 1), (3, 1)]
    assert compress([1, 1, 1, 2, 2, 2, 3, 3, 3]) == [(1, 3), (2, 3), (3, 3)]
    assert compress("") == []
    assert compress("abc") == [("a", 1), ("b", 1), ("c", 1)]
    assert compress("aaa") == [("a", 3)]
    assert compress("aaabbbcccxxxxxxxxxx") == [("a", 3), ("b", 3), ("c", 3), ("x", 10)]


def test_element_by_index():
    assert element_by_index([(1, 3), (2, 3)], 1) == 1
    assert element_by_index([(1, 3), (2, 3)], 3) == 2
    with pytest.raises(ValueError):
        element_by_index([(1, 3), (2, 3)], 6)


def test_element_by_index2():
    assert element_by_index2([(1, 3), (2, 3)], 1) == 1
    assert element_by_index2([(1, 3), (2, 3)], 3) == 2
    with pytest.raises(ValueError):
        element_by_index([(1, 3), (2, 3)], 6)
