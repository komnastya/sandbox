from zigzag import zig_zag, zig_zag_2


def test_zig_zag():
    assert zig_zag(-1) == []
    assert zig_zag(0) == [0]
    assert zig_zag(1) == [0, -1]
    assert zig_zag(5) == [0, -1, 2, -3, 4, -5]


def test_zig_zag_2():
    assert zig_zag_2(-1) == []
    assert zig_zag_2(0) == []
    assert zig_zag_2(1) == [1, -1]
    assert zig_zag_2(5) == [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]
