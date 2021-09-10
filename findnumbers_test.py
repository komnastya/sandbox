from findnumbers import find_numbers


def test_findnumbers():
    assert find_numbers("") == []
    assert find_numbers("no numbers here") == []
    assert find_numbers("0") == [0]
    assert find_numbers("012") == [12]
    assert find_numbers("0 1 2") == [0, 1, 2]
    assert find_numbers("0,1,2,") == [0, 1, 2]
    assert find_numbers("(123)") == [123]
    assert find_numbers("12some34numbers56here78") == [12, 34, 56, 78]
    assert find_numbers("-1+2") == [1, 2]
