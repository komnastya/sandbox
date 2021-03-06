from negative_numbers_search import count_negative_numbers, count_negative_numbers_2


def test_negative_numbers_search():
    assert count_negative_numbers([[]]) == 0
    assert count_negative_numbers([[2], [1]]) == 0
    assert count_negative_numbers([[-1]]) == 1
    assert count_negative_numbers([[1], [-1]]) == 1
    assert count_negative_numbers([[-1], [-2]]) == 2
    assert count_negative_numbers([[2, 1], [-1, -2]]) == 2
    assert count_negative_numbers([[1, 2], [1, -1], [-1, -2]]) == 3
    assert count_negative_numbers([[5, 4, 3, 2, -1], [-1, -2, -3, -4, -5]]) == 6
    assert count_negative_numbers([[4, 3], [2, -1], [-1, -2]]) == 3
    assert count_negative_numbers([[1, -1], [-2, -3], [-4, -5]]) == 5
    assert count_negative_numbers([[4, 3, 2], [1, -1, -1]]) == 2


def test_negative_numbers_search_2():
    assert count_negative_numbers_2([[]]) == 0
    assert count_negative_numbers_2([[2], [1]]) == 0
    assert count_negative_numbers_2([[-1]]) == 1
    assert count_negative_numbers_2([[1], [-1]]) == 1
    assert count_negative_numbers_2([[-1], [-2]]) == 2
    assert count_negative_numbers_2([[2, 1], [-1, -2]]) == 2
    assert count_negative_numbers_2([[1, 2], [1, -1], [-1, -2]]) == 3
    assert count_negative_numbers_2([[5, 4, 3, 2, -1], [-1, -2, -3, -4, -5]]) == 6
    assert count_negative_numbers_2([[4, 3], [2, -1], [-1, -2]]) == 3
    assert count_negative_numbers_2([[1, -1], [-2, -3], [-4, -5]]) == 5
    assert count_negative_numbers_2([[4, 3, 2], [1, -1, -1]]) == 2
