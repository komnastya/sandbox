from movezeroes import moveZeroes


def test_moveZeroes():
    nums = [0, 1, 0, 1, 0]
    moveZeroes(nums)
    assert nums == [1, 1, 0, 0, 0]

    nums = [1, 1, 1, 0, 0]
    moveZeroes(nums)
    assert nums == [1, 1, 1, 0, 0]

    nums = [1, 1, 1, 1, 1]
    moveZeroes(nums)
    assert nums == [1, 1, 1, 1, 1]

    nums = [0, 0, 0, 0, 0]
    moveZeroes(nums)
    assert nums == [0, 0, 0, 0, 0]
