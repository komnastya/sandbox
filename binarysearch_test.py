from binarysearch import binary_search


def test_binarysearch():
    assert binary_search([0, 1, 2, 3, 4, 5], 6) == -1
    assert binary_search([0, 1, 2, 3, 4, 5], 5) == 5
    assert binary_search([], 1) == -1
