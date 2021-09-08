from triangle_iterator import triangle


def test_finite_iterator_of_iterators():
    finite_iterator = iter(triangle(3))
    list_of_lists = [list(inner_iterator) for inner_iterator in finite_iterator]
    assert list_of_lists == [[], [1], [1, 2]]


def test_empty_iterator():
    finite_iterator = iter(triangle(0))
    assert list(finite_iterator) == []


def test_infinite_iterator_of_iterators():
    infinite_iterator = iter(triangle())
    assert list(next(infinite_iterator)) == []
    assert list(next(infinite_iterator)) == [1]
    assert list(next(infinite_iterator)) == [1, 2]
    assert list(next(infinite_iterator)) == [1, 2, 3]
