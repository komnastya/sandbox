from typing import Generator, List


# A function which generates Fibonacci sequence in which
# the last member is not larger  than the given max.
def fibonacci(max: int) -> List[int]:
    if max <= 0:
        raise ValueError
    a = 0
    b = 1
    output = []
    output.append(a)
    output.append(b)
    while True:
        c = a + b
        if c > max:
            break
        output.append(c)
        a = b
        b = c
    return output


# An iterable class which generates infinite Fibonacci sequence.
class Fibonacci:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        c = self.a + self.b
        self.a = self.b
        self.b = c
        return self.a


# A generator which generates infinite Fibonacci sequence.
def fibonacci_g() -> Generator[int, None, None]:
    yield 1
    a = 0
    b = 1
    while True:
        c = a + b
        yield c
        a = b
        b = c
