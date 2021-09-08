from majority_element import majority_element, majority_element_for, majority_element_while


def test_majority_element_for():
    assert majority_element_for([]) == None
    assert majority_element_for([1]) == 1
    assert majority_element_for([1, 1, 1]) == 1
    assert majority_element_for([3, 2, 3]) == 3
    assert majority_element_for([2, 2, 1, 1, 1, 2, 2]) == 2


def test_majority_element_while():
    assert majority_element_while([]) == None
    assert majority_element_while([1]) == 1
    assert majority_element_while([1, 1, 1]) == 1
    assert majority_element_while([3, 2, 3]) == 3
    assert majority_element_while([2, 2, 1, 1, 1, 2, 2]) == 2


def test_majority_element():
    assert majority_element([1]) == 1
    assert majority_element([1, 1, 1]) == 1
    assert majority_element([3, 2, 3]) == 3
    assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2
