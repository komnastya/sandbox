from truncate import truncate, truncate_2, truncate_3


def test_truncate():
    assert truncate([], 3) == []
    assert truncate([1, 2, 3, 4, 5, 6], 3) == [1, 2, 3]
    assert truncate([1, 2, 3, 4, 5, 6], 0) == []
    assert truncate([1, 2, 3], 1_000_000) == [1, 2, 3]


def test_truncate_2():
    nums = [1, 2, 3, 4, 5, 6]
    truncate_2(nums, 3)
    assert nums == [1, 2, 3]

    nums = [1, 2, 3, 4, 5, 6]
    truncate_2(nums, 0)
    assert nums == []

    nums = [1, 2, 3, 4, 5, 6]
    truncate_2(nums, 1000)
    assert nums == [1, 2, 3, 4, 5, 6]

    nums = []
    truncate_2(nums, 1000)
    assert nums == []


def test_truncate_3():
    nums = [1, 2, 3, 4, 5, 6]
    truncate_3(nums, 3)
    assert nums == [1, 2, 3]

    nums = [1, 2, 3, 4, 5, 6]
    truncate_3(nums, 0)
    assert nums == []

    nums = [1, 2, 3, 4, 5, 6]
    truncate_3(nums, 1000)
    assert nums == [1, 2, 3, 4, 5, 6]

    nums = []
    truncate_3(nums, 1000)
    assert nums == []
