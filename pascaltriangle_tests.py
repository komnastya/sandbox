from pascaltriangle import pascal_triangle, pascal_triangle_by_index


def test_PascalTriangle():
    assert pascal_triangle(-1) == []
    assert pascal_triangle(1) == [[1]]
    assert pascal_triangle(2) == [[1], [1, 1]]
    assert pascal_triangle(3) == [[1], [1, 1], [1, 2, 1]]
    assert pascal_triangle(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]


def test_PascalTriangleByIndex():
    assert pascal_triangle_by_index(0) == [1]
    assert pascal_triangle_by_index(1) == [1, 1]
    assert pascal_triangle_by_index(2) == [1, 2, 1]
    assert pascal_triangle_by_index(3) == [1, 3, 3, 1]
