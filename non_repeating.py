# [1,2,3,4,5] -> [1,2,3,4,5]
# [1,2,1,2,1] -> [1,2,1,2,1]
# [1,1,1,1,1] -> [1]
# [1,1,2,2,2] -> [1,2]
#
# If `it` is sorted, then obviously this function generates only unique elements.
# If `it` is not sorted, then the generated elements are not unique in the whole sequence,
# but there are no equal consecutive elements.
def non_repeating(it):
    """Yields elements from it, but only thise which are not repeating."""
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
