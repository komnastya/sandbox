import pytest

from set import MySet


def test_init():
    assert set(MySet()) == set()
    assert set(MySet({1, 2, 3})) == {1, 2, 3}


def test_add():
    s = MySet()
    assert set(s) == set()
    s.add(1)
    s.add(11)
    assert set(s) == {1, 11}


def test_clear():
    s = MySet()
    s.add(1)
    s.add(2)
    s.add(3)
    assert set(s) == {1, 2, 3}

    s.clear()
    assert set(s) == set()
    assert s.len == 0


def test_copy():
    a = MySet()

    a.add(1)
    a.add(2)
    a.add(3)

    assert set(a) == {1, 2, 3}

    b = a.copy()

    a.add(4)
    b.remove(3)

    assert set(a) == {1, 2, 3, 4}
    assert set(b) == {1, 2}


def test_add_duplicates():
    s = MySet()
    assert set(s) == set()
    s.add(1)
    s.add(1)
    s.add(1)
    assert set(s) == {1}


def test_discard():
    s = MySet()
    s.add(1)
    assert 1 in s
    s.discard(1)
    assert not 1 in s
    s.add(1)
    assert 1 in s
    s.discard(1)
    assert not 1 in s


def test_remove():
    s = MySet()
    assert set(s) == set()

    s.add(1)
    assert set(s) == {1}

    s.remove(1)
    assert set(s) == set()

    with pytest.raises(KeyError):
        s.remove(2)


def test_pop():
    s = MySet()
    s.add(1)
    s.add(2)
    s.add(3)

    assert len(s) == 3

    a = s.pop()

    assert a == 1
    assert not a in s
    assert len(s) == 2

    s.pop()
    s.pop()

    with pytest.raises(KeyError):
        s.pop()


def test_has():
    s = MySet()
    assert not 1 in s
    s.add(1)
    assert 1 in s


def test_equality():
    a = MySet()
    b = MySet()

    assert a != list()
    assert a != set()
    assert a != tuple()
    assert a != frozenset()

    assert a == a
    assert b == b
    assert a == b

    a.add(1)
    assert a != b

    b.add(1)
    assert a == b


def test_iterator():
    s = MySet()
    s.add(1)
    s.add(2)
    s.add(3)
    assert set(s) == {1, 2, 3}


def test_len():
    s = MySet()
    assert len(s) == 0
    s.add(1)
    s.add(2)
    s.add(3)
    assert len(s) == 3
    s.discard(3)
    assert len(s) == 2


def test_str():
    s = MySet()
    assert str(s) == "{}"
    s.add(1)
    s.add(2)
    s.add(3)

    assert str(s) == "{1, 2, 3}"


def test_union():
    a = MySet()
    b = MySet()

    assert set(a.union(b)) == set()

    for x in range(0, 4):
        a.add(x)

    assert set(a.union(b)) == {0, 1, 2, 3}

    for x in range(2, 6):
        b.add(x)

    assert set(a.union(b)) == {0, 1, 2, 3, 4, 5}


def test_or_operator():
    a = MySet()
    b = MySet()

    assert set(a | b) == set()

    for x in range(0, 4):
        a.add(x)

    assert set(a | b) == {0, 1, 2, 3}

    for x in range(2, 6):
        b.add(x)

    assert set(a | b) == {0, 1, 2, 3, 4, 5}


def test_union_update():
    a = MySet()
    b = MySet()

    a.update(b)
    assert set(a) == set()

    for x in range(0, 4):
        a.add(x)

    a.update(b)
    assert set(a) == {0, 1, 2, 3}

    for x in range(2, 6):
        b.add(x)

    a.update(b)
    assert set(a) == {0, 1, 2, 3, 4, 5}

    b.update(a)
    assert set(b) == {0, 1, 2, 3, 4, 5}


def test_ior_operator():
    a = MySet()
    b = MySet()

    for x in range(1, 5):
        a.add(x)

    for y in range(3, 8):
        b.add(y)

    a |= b
    assert set(a) == {1, 2, 3, 4, 5, 6, 7}

    b |= a
    assert set(a) == {1, 2, 3, 4, 5, 6, 7}


def test_intersection():
    a = MySet()
    b = MySet()

    assert set(a.intersection(b)) == set()

    for x in range(0, 4):
        a.add(x)

    assert set(a.intersection(b)) == set()

    for x in range(2, 6):
        b.add(x)

    assert set(a.intersection(b)) == {2, 3}


def test_and_operator():
    a = MySet()
    b = MySet()

    assert set(a & b) == set()

    for x in range(0, 4):
        a.add(x)

    assert set(a & b) == set()

    for x in range(2, 6):
        b.add(x)

    assert set(a & b) == {2, 3}


def test_intersection_update():
    a = MySet()
    b = MySet()

    a.intersection_update(b)
    assert set(a) == set()

    for x in range(0, 4):
        a.add(x)

    a.intersection_update(b)
    assert set(a) == set()

    for x in range(0, 4):
        a.add(x)

    for x in range(2, 6):
        b.add(x)

    a.intersection_update(b)
    assert set(a) == {2, 3}

    b.intersection_update(a)
    assert set(b) == {2, 3}


def test_iand_operator():
    a = MySet()
    b = MySet()

    a &= b
    assert set(a) == set()

    for x in range(0, 4):
        a.add(x)

    a &= b
    assert set(a) == set()

    for x in range(0, 4):
        a.add(x)

    for x in range(2, 6):
        b.add(x)

    a &= b
    assert set(a) == {2, 3}

    b &= a
    assert set(b) == {2, 3}


def test_difference():
    a = MySet()
    b = MySet()

    assert set(a.difference(b)) == set()

    for x in range(0, 4):
        a.add(x)

    assert set(a.difference(b)) == {0, 1, 2, 3}

    for x in range(2, 6):
        b.add(x)

    assert set(a.difference(b)) == {0, 1}
    assert set(b.difference(a)) == {4, 5}


def test_sub_operator():
    a = MySet()
    b = MySet()

    assert set(a - b) == set()

    for x in range(0, 4):
        a.add(x)

    assert set(a - b) == {0, 1, 2, 3}

    for x in range(2, 6):
        b.add(x)

    assert set(a - b) == {0, 1}
    assert set(b - a) == {4, 5}


def test_difference_update():
    a = MySet()
    b = MySet()

    a.difference_update(b)
    assert set(a) == set()

    for x in range(0, 4):
        a.add(x)

    a.difference_update(b)
    assert set(a) == {0, 1, 2, 3}

    for x in range(2, 6):
        b.add(x)

    a.difference_update(b)
    assert set(a) == {0, 1}

    a.difference_update(b)
    assert set(b) == {2, 3, 4, 5}


def test_isub_operator():
    a = MySet()
    b = MySet()

    a -= b
    assert set(a) == set()

    for x in range(0, 4):
        a.add(x)

    a -= b
    assert set(a) == {0, 1, 2, 3}

    for x in range(2, 6):
        b.add(x)

    a -= b
    assert set(a) == {0, 1}

    b -= a
    assert set(b) == {2, 3, 4, 5}


def test_symmetric_difference():
    a = MySet()
    b = MySet()

    assert set(a.symmetric_difference(b)) == set()

    for x in range(0, 4):
        a.add(x)

    assert set(a.symmetric_difference(b)) == {0, 1, 2, 3}

    for x in range(2, 6):
        b.add(x)

    assert set(a.symmetric_difference(b)) == {0, 1, 4, 5}


def test_xor_operator():
    a = MySet()
    b = MySet()

    assert set(a ^ b) == set()

    for x in range(0, 4):
        a.add(x)

    assert set(a ^ b) == {0, 1, 2, 3}

    for x in range(2, 6):
        b.add(x)

    assert set(a ^ b) == {0, 1, 4, 5}


def test_ixor_operator():
    a = MySet()
    b = MySet()

    a ^= b
    assert set(a) == set()

    for x in range(0, 4):
        a.add(x)

    a ^= b
    assert set(a) == {0, 1, 2, 3}

    for x in range(2, 6):
        b.add(x)

    a ^= b
    assert set(a) == {0, 1, 4, 5}

    b ^= a
    assert set(b) == {0, 1}


def test_isdisjoint():
    a = MySet()
    b = MySet()

    for x in range(11):
        a.add(x)

    for x in range(20, 29):
        b.add(x)

    assert a.isdisjoint(b) == True

    for x in range(1, 10):
        b.add(x)

    assert a.isdisjoint(b) == False


def test_issubset():
    a = MySet()
    b = MySet()

    for x in range(3):
        a.add(x)

    assert a.issubset(b) == False

    for x in range(5):
        b.add(x)

    assert a.issubset(b) == True
    assert b.issubset(a) == False


def test_issuperset():
    a = MySet()
    b = MySet()

    for x in range(7):
        a.add(x)

    assert a.issuperset(b) == True

    for x in range(3):
        b.add(x)

    assert a.issuperset(b) == True
    assert b.issuperset(a) == False
    assert b.issubset(a) == True
