# Returns the first `count` elements from the given iterable.
def head(it, count):
    it = iter(it)
    while count > 0:
        try:
            yield next(it)
        except StopIteration:
            break
        count -= 1


# Skips the first `count` elements from the given iterable and returns all the remaining elements.
def skip(it, count):
    it = iter(it)
    while True:
        try:
            a = next(it)
        except StopIteration:
            break
        if count > 0:
            count -= 1
        else:
            yield a


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
