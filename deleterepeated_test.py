from deleterepeated import delete_repeated, delete_repeated_2, removeDuplicates


def test_delete_repeated():
    list = [1, 2, 3]
    delete_repeated(list)
    assert list == [1, 2, 3]

    list = [1, 1, 2, 2, 1, 1]
    delete_repeated(list)
    assert list == [1, 2, 1]

    list = [1, 1, 1, 1]
    delete_repeated(list)
    assert list == [1]


def test_delete_repeated_2():
    assert delete_repeated_2([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert delete_repeated_2([1, 1, 2, 2, 1, 1]) == [1, 2, 1]
    assert delete_repeated_2([1, 1, 1]) == [1]


def test_removeDuplicates():
    nums = []
    removeDuplicates(nums)
    assert nums == []

    nums = [1, 1, 2, 2, 1, 1]
    removeDuplicates(nums)
    assert nums == [1, 2, 1]

    nums = [1, 2, 3, 4, 5]
    removeDuplicates(nums)
    assert nums == [1, 2, 3, 4, 5]
