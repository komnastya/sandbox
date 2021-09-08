from sumoddlenghtsubarrays import sumOddLengthSubarrays


def test_sumoddlengthsubarrays():
    assert sumOddLengthSubarrays([]) == 0
    assert sumOddLengthSubarrays([1]) == 1
    assert sumOddLengthSubarrays([1, 2]) == 3
    assert sumOddLengthSubarrays([1, 2, 3]) == 12
    assert sumOddLengthSubarrays([1, 2, 3, 4]) == 25
    assert sumOddLengthSubarrays([-1, -2, -3, -4]) == -25
