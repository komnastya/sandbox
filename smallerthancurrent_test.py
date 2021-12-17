from smallerthancurrent import smallerNumbersThanCurrent, smallerNumbersThanCurrent_slow


def test_smallerNumbersThanCurrent():
    assert smallerNumbersThanCurrent([]) == []
    assert smallerNumbersThanCurrent([1, 2, 3, 4, 5]) == [0, 1, 2, 3, 4]
    assert smallerNumbersThanCurrent([1, 1, 1, 1]) == [0, 0, 0, 0]
    assert smallerNumbersThanCurrent([9, 5, 3, 7, 11]) == [3, 1, 0, 2, 4]


def test_smallerNumbersThanCurrent_slow():
    assert smallerNumbersThanCurrent_slow([]) == []
    assert smallerNumbersThanCurrent_slow([1, 2, 3, 4, 5]) == [0, 1, 2, 3, 4]
    assert smallerNumbersThanCurrent_slow([1, 1, 1, 1]) == [0, 0, 0, 0]
    assert smallerNumbersThanCurrent_slow([9, 5, 3, 7, 11]) == [3, 1, 0, 2, 4]
