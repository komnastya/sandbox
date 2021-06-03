# [1,2,3,4,5] -> [1,2,3,4,5]
# [1,2,1,2,1] -> [1,2,1,2,1]
# [1,1,1,1,1] -> [1]
# [1,1,2,2,2] -> [1,2]
#
# If `it` is sorted, then obviously this function generates only unique elements.
# If `it` is not sorted, then the generated elements are not unique in the whole sequence,
# but there are no equal consecutive elements.
def non_repeating_one(it):
    it = iter(it)
    x = next(it, None)
    while x is not None:
        y = x
        x = next(it, None)
        if x != y:
            yield y


def non_repeating_two(it):
    it = iter(it)
    x = next(it, None)
    y = next(it, None)
    while x is not None and y is not None:
        if x != y:
            yield x
        x = y
        y = next(it, None)
    if x is not None:
        yield x


def non_repeating_better(it):
    it = iter(it)
    last = None
    has_last = False
    while True:
        try:
            current = next(it)
        except StopIteration:
            break
        if not has_last or current != last:
            yield current
        last = current
        has_last = True
