from pushback import PushBackIterator


# Merges two sorted sequences of numbers into a single sorted sequence.
#
# merge([], []) -> []
# merge([1, 2, 3], []) -> [1, 2, 3]
# merge([], [1, 2, 3]) -> [1, 2, 3]
# merge([1], [2]) -> [1, 2]
# merge([2], [1]) -> [1, 2]
# merge([1, 3, 5], [2, 4, 6]) -> [1, 2, 3, 4, 5, 6]
# merge([2, 4, 6], [1, 3, 5]) -> [1, 2, 3, 4, 5, 6]
# merge([1, 1, 1], [2, 2, 2]) -> [1, 1, 1, 2, 2, 2]
#
# Both `a` and `b` are iterables, and the result must be iterable too. Don't use lists! Use `yield`.
# Both `a` and `b` are sorted, and the result must be sorted too.


# Without PushBackIterator


def merge_ugly(a, b):
    a = iter(a)
    b = iter(b)
    x = next(a, None)
    y = next(b, None)
    while x is not None and y is not None:
        if x <= y:
            yield x
            x = next(a, None)
        else:
            yield y
            y = next(b, None)
    if x is not None:
        yield x
    if y is not None:
        yield y
    yield from a
    yield from b


# Using PushBackIterator


def merge(a, b):
    a = PushBackIterator(iter(a))
    b = PushBackIterator(iter(b))
    while True:
        try:
            x = next(a)
        except StopIteration:
            break
        try:
            y = next(b)
        except StopIteration:
            a.push_back(x)
            break
        if x <= y:
            yield x
            b.push_back(y)
        else:
            yield y
            a.push_back(x)
    yield from a
    yield from b


# Using PushBackIterator with implemented has_next method


def merge_better(a, b):
    a = PushBackIterator(iter(a))
    b = PushBackIterator(iter(b))
    while a.has_next() and b.has_next():
        x = next(a)
        y = next(b)
        if x <= y:
            yield x
            b.push_back(y)
        else:
            yield y
            a.push_back(x)
    yield from a
    yield from b
