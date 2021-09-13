import pytest

from dict import MyDict


def test_dict():
    d = MyDict()

    assert len(d) == 0
    assert str(d) == "{}"
    assert 1 not in d
    assert d.get(1) is None

    d.set(1, "one")

    assert len(d) == 1
    assert str(d) == "{1: one}"
    assert 1 in d
    assert d.get(1) == "one"

    d.set(1, "uno")

    assert len(d) == 1
    assert str(d) == "{1: uno}"
    assert 1 in d
    assert d.get(1) == "uno"

    d.set(3, "tre")
    d.set(2, "due")

    assert len(d) == 3
    assert str(d) == "{1: uno, 2: due, 3: tre}"
    assert 1 in d
    assert d.get(1) == "uno"
    assert 2 in d
    assert d.get(2) == "due"
    assert 3 in d
    assert d.get(3) == "tre"


def test_get():
    d = MyDict()
    d.set(1, "one")
    d.set(2, "two")
    d.set(3, "three")

    assert d.get(1) == "one"
    assert d.get(2) == "two"
    assert d.get(3) == "three"
    assert d.get(4) is None


def test_getitem():
    d = MyDict()

    with pytest.raises(KeyError):
        d[1]

    d.set(1, "one")
    d.set(2, "two")
    d.set(3, "three")

    assert d[1] == "one"
    assert d[2] == "two"
    assert d[3] == "three"


def test_setitem():
    d = MyDict()

    assert len(d) == 0
    assert str(d) == "{}"
    assert 1 not in d
    assert d.get(1) is None

    d[1] = "one"
    d[2] = "two"

    assert len(d) == 2
    assert str(d) == "{1: one, 2: two}"
    assert 1 in d
    assert 2 in d
    assert d.get(1) == "one"
    assert d.get(2) == "two"


def test_delitem():
    d = MyDict()

    assert len(d) == 0
    assert str(d) == "{}"
    assert 1 not in d
    assert d.get(1) is None

    d[1] = "one"
    d[2] = "two"

    assert len(d) == 2
    assert str(d) == "{1: one, 2: two}"

    del d[1]
    del d[2]

    assert len(d) == 0
    assert str(d) == "{}"

    with pytest.raises(KeyError):
        del d[1]


def test_pop():
    d = MyDict()

    d[1] = "one"

    assert d.pop(1) == "one"

    with pytest.raises(KeyError):
        d.pop(2)

    assert d.pop(3, "Not found") == "Not found"


def test_setdefault():
    d = MyDict()

    d[1] = "one"

    assert d.setdefault(1) == "one"
    assert d.setdefault(1, "uno") == "one"
    assert d.setdefault(2) is None
    assert d.setdefault(2, "two") == "two"


def test_popitem():
    d = MyDict()

    d.set(1, "one")
    d.set(2, "two")

    assert len(d) == 2

    a = d.popitem()
    a_key = a[0]

    assert a == (1, "one")
    assert a_key not in d
    assert len(d) == 1

    b = d.popitem()
    b_key = b[0]
    assert b == (2, "two")
    assert b_key not in d
    assert len(d) == 0

    with pytest.raises(KeyError):
        d.popitem()


def test_len():
    d = MyDict()
    assert len(d) == 0

    d.set(1, "one")
    d.set(2, "two")
    d.set(3, "three")

    assert len(d) == 3


def test_contains():
    d = MyDict()

    assert 1 not in d
    d[1] = "one"
    assert 1 in d

    d_items = d.items()
    assert 1 in d_items
    assert "one" not in d_items

    d_keys = d.keys()
    assert 1 in d_keys
    assert "one" not in d_keys

    d_values = d.values()
    assert "one" in d_values
    assert 1 not in d_values


def test_str():
    d = MyDict()

    assert str(d) == "{}"

    d.set(1, "one")
    d.set(2, "two")

    assert str(d) == "{1: one, 2: two}"


def test_clear():
    d = MyDict()

    d.set(1, "one")
    d.set(2, "two")

    assert str(d) == "{1: one, 2: two}"

    d.clear()
    assert str(d) == "{}"


def test_copy():
    d = MyDict()

    d.set(1, "one")
    d.set(2, "two")
    assert str(d) == "{1: one, 2: two}"

    dd = d.copy()
    del d[2]
    dd[3] = "three"
    assert str(d) == "{1: one}"
    assert str(dd) == "{1: one, 2: two, 3: three}"


def test_fromkeys():
    assert str(MyDict().fromkeys([1, 2, 3])) == "{1: None, 2: None, 3: None}"
    assert (
        str(MyDict().fromkeys([1, 2, 3], "number"))
        == "{1: number, 2: number, 3: number}"
    )


def test_dictitems():
    d = MyDict()
    assert str(d.items()) == "dict_items[]"

    d[1] = "one"
    d[2] = "two"

    assert str(d.items()) == "dict_items[(1, one), (2, two)]"
    assert len(d.items()) == 2


def test_dictkeys():
    d = MyDict()
    assert str(d.keys()) == "dict_keys[]"

    d[1] = "one"
    d[2] = "two"

    assert str(d.keys()) == "dict_keys[1, 2]"
    assert len(d.keys()) == 2


def test_dictvalues():
    d = MyDict()
    assert str(d.values()) == "dict_values[]"

    d[1] = "one"
    d[2] = "two"

    assert str(d.values()) == "dict_values[one, two]"
    assert len(d.values()) == 2


def test_documentation():
    d = MyDict()

    assert d.__doc__ == "My own dictionary class"

    items = d.items()
    assert items.__doc__ == "My class for dictionary items"

    keys = d.keys()
    assert keys.__doc__ == "My class for dictionary keys"

    values = d.values()
    assert values.__doc__ == "My class for dictionary values"


def test_eq():
    d = MyDict()
    dd = d
    c = MyDict()

    assert d == dd
    assert c == d
    assert c == dd

    assert d is dd
    assert c is not d
    assert c is not dd

    d[1] = "one"
    dd[2] = "two"
    c[3] = "three"

    assert d, dd
    assert d is dd
    assert c != d
    assert c != dd

    c[3] = "one"
    c[4] = "two"

    assert c is not d
    assert c != d
    assert c is not dd
    assert c != dd
    assert d is dd
    assert d == dd


def test_update():
    d = MyDict()
    d[1] = "one"
    d[2] = "three"

    d1 = MyDict()
    d1[2] = "two"
    assert str(d) == "{1: one, 2: three}"

    d.update(d1)
    assert str(d) == "{1: one, 2: two}"

    d1[3] = "three"
    d.update(d1)
    assert str(d) == "{1: one, 2: two, 3: three}"
