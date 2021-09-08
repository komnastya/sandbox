import pytest

from fibonacci import Fibonacci, fibonacci, fibonacci_g


def test_fibonacci_seq():
    assert fibonacci(1) == [0, 1, 1]
    assert fibonacci(8) == [0, 1, 1, 2, 3, 5, 8]
    assert fibonacci(15) == [0, 1, 1, 2, 3, 5, 8, 13]
    with pytest.raises(ValueError):
        fibonacci(-1)


def test_fibonacci_class():
    seq = Fibonacci()
    assert next(seq) == 1
    assert next(seq) == 1
    assert next(seq) == 2
    assert next(seq) == 3
    assert next(seq) == 5
    assert next(seq) == 8


def test_fibonacci_generator():
    seq = fibonacci_g()
    assert next(seq) == 1
    assert next(seq) == 1
    assert next(seq) == 2
    assert next(seq) == 3
    assert next(seq) == 5
    assert next(seq) == 8
