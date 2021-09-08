from fizzbuzz import fizz_buzz


def test_fizzbuzz():
    assert fizz_buzz(0) == []
    assert fizz_buzz(1) == [1]
    assert fizz_buzz(15) == [
        1,
        2,
        (3, "fizz"),
        4,
        (5, "buzz"),
        (6, "fizz"),
        7,
        8,
        (9, "fizz"),
        (10, "buzz"),
        11,
        (12, "fizz"),
        13,
        14,
        (15, "fizz_buzz"),
    ]
