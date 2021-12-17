from powers import powers_of_three, powers_of_two


def test_powers_of_two():
    assert powers_of_two(0) == []
    assert powers_of_two(1) == [1]
    assert powers_of_two(2) == [1, 2]
    assert powers_of_two(5) == [1, 2, 4]
    assert powers_of_two(8) == [1, 2, 4, 8]
    assert powers_of_two(-1) == []


def test_powers_of_three():
    assert powers_of_three(0) == []
    assert powers_of_three(1) == [1]
    assert powers_of_three(3) == [1, 3]
    assert powers_of_three(33) == [1, 3, 9, 27]
    assert powers_of_three(-1) == []
