from digits import digits_to_number, number_to_digits


def test_DigitsToNumber():
    assert digits_to_number([]) == 0
    assert digits_to_number([0]) == 0
    assert digits_to_number([1]) == 1
    assert digits_to_number([1, 0]) == 10
    assert digits_to_number([1, 2, 3, 4, 5]) == 12345


def test_NumberToDigits():
    assert number_to_digits(0) == [0]
    assert number_to_digits(1) == [1]
    assert number_to_digits(10) == [1, 0]
    assert number_to_digits(12345) == [1, 2, 3, 4, 5]
    assert number_to_digits(256, 2) == [1, 0, 0, 0, 0, 0, 0, 0, 0]
