from typing import Generator, List


# Fibonacci sequence
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


# Fibonacci class
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


# Fibonacci generator
def fibonacci_g() -> Generator[int, None, None]:
    yield 1
    a = 0
    b = 1
    while True:
        c = a + b
        yield c
        a = b
        b = c
