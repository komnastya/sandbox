from largesttriangleperimeter import largestPerimeter


def test_find():
    assert largestPerimeter([]) == 0
    assert largestPerimeter([1, 2, 1]) == 0
    assert largestPerimeter([2, 1, 2]) == 5
    assert largestPerimeter([3, 2, 3, 4]) == 10
    assert largestPerimeter([3, 6, 2, 3]) == 8
