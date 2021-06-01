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


# Returns the first `count` elements from the given iterable.
def head(it, count):
    it = iter(it)
    while count > 0:
        try:
            yield next(it)
        except StopIteration:
            break
        count -= 1


print("head of an empty list:", list(head([], 10)))
print("head of a  short list:", list(head([1, 2, 3], 10)))
print("empty head of  a list:", list(head([1, 2, 3], 0)))
print("head(Fibonacci) result:", list(head(Fibonacci(), 10)))
print("head(fibonacci) result:", list(head(fibonacci(), 10)))


# Skips the first `count` elements from the given iterable and returns all the remaining elements.
def skip(it, count):
    while True:
        try:
            a = next(it)
        except StopIteration:
            break
        if count > 0:
            count -= 1
        else:
            yield a


print("skip(head(...), ...) function result")
print(list(skip(head(fibonacci(), 10), 10)))
print("head(skip(...), ...) function result")
print(list(head(skip(fibonacci(), 10), 10)))


# From the given iterable returns elements in even positions.
# [a, b, c, d, e, f] -> [a, c, e]
def even(it):
    it = iter(it)
    while True:
        try:
            yield next(it)
            next(it)
        except StopIteration:
            break


print("even function result")
print(list(even(["a", "b", "c", "d", "e", "f"])))


# From the given iterable returns elements in odd positions.
# [a, b, c, d, e, f] -> [b, d, f]
def odd(it):
    it = iter(it)
    while True:
        try:
            next(it)
            yield next(it)
        except StopIteration:
            break


print("odd function result")
print(list(odd(["a", "b", "c", "d", "e", "f"])))

print("--- first 10 Fibonacci numbers")
print(list(head(fibonacci(), 10)))

print("--- first 10 Fibonacci numbers that are in the even positions")
print(list(head(even(fibonacci()), 10)))

print("--- first 10 Fibonacci numbers ...")
print(list(even(head(fibonacci(), 10))))

print("--- first 10 Fibonacci numbers that are in the odd positions")
print(list(head(odd(fibonacci()), 10)))

print("--- first 10 Fibonacci numbers ...")
print(list(odd(head(fibonacci(), 10))))
