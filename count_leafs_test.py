from count_leafs import count_leaf_items, count_leaf_items_recursive


def test_count_leafs_recursive():
    assert count_leaf_items_recursive([]) == 0
    assert count_leaf_items_recursive([1]) == 1
    assert count_leaf_items_recursive([1, 2]) == 2
    assert count_leaf_items_recursive([1, [2]]) == 2
    assert count_leaf_items_recursive([1, [2, [3]]]) == 3
    assert count_leaf_items_recursive([[1], [2], [3]]) == 3


def test_count_leafs():
    assert count_leaf_items([]) == 0
    assert count_leaf_items([1]) == 1
    assert count_leaf_items([1, 2]) == 2
    assert count_leaf_items([1, [2]]) == 2
    assert count_leaf_items([1, [2, [3]]]) == 3
    assert count_leaf_items([[1], [2], [3]]) == 3
