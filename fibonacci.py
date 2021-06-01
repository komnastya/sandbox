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


def fibonacci():
    yield 1
    a = 0
    b = 1
    while True:
        c = a + b
        yield c
        a = b
        b = c
