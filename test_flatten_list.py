import pytest
from flatten_list import flatten_list, flatten_list2


def test_flatten_list():
    assert flatten_list([]) == []
    assert flatten_list([[], [[]]]) == []
    assert flatten_list([1, 2, 3]) == [1, 2, 3]
    assert flatten_list([1, 2, 3]) == [1, 2, 3]
    assert flatten_list([1, [2, [3]]]) == [1, 2, 3]
    assert flatten_list([[[[[1, 2, 3]]]]]) == [1, 2, 3]

    assert flatten_list([1, [2, [3]]], depth=0) == [1, [2, [3]]]
    assert flatten_list([1, [2, [3]]], depth=1) == [1, 2, [3]]
    assert flatten_list([1, [2, [3, [4]]]], depth=2) == [1, 2, 3, [4]]
    assert flatten_list([1, [2, [3, [4]]]], depth=3) == [1, 2, 3, 4]


def test_flatten_list2():
    assert flatten_list2([]) == []
    assert flatten_list2([[], [[]]]) == []
    assert flatten_list2([1, 2, 3]) == [1, 2, 3]
    assert flatten_list2([1, 2, 3]) == [1, 2, 3]
    assert flatten_list2([1, [2, [3]]]) == [1, 2, 3]
    assert flatten_list2([[[[[1, 2, 3]]]]]) == [1, 2, 3]

    assert flatten_list2([1, [2, [3]]], depth=0) == [1, [2, [3]]]
    assert flatten_list2([1, [2, [3]]], depth=1) == [1, 2, [3]]
    assert flatten_list2([1, [2, [3, [4]]]], depth=2) == [1, 2, 3, [4]]
    assert flatten_list2([1, [2, [3, [4]]]], depth=3) == [1, 2, 3, 4]
