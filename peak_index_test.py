from peak_index import peak_index


def test_peak_index():
    assert peak_index([0, 1, 0]) == 1
    assert peak_index([1, 3, 5, 7, 9, 11, 6, 3]) == 5
