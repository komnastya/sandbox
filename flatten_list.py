# Given a list of lists of lists of items (of arbitrary depth)
# this function returns a single flat list of items.


def flatten_list(items, depth=1000):
    output = []
    for item in items:
        if isinstance(item, list) and depth > 0:
            output.extend(flatten_list2(item, depth - 1))
        else:
            output.append(item)
    return output


def flatten_list2(items, depth=None):
    output = []
    if depth is None:
        depth = 1000

    def step(items, depth):
        for item in items:
            if isinstance(item, list) and depth > 0:
                step(item, depth - 1)
            else:
                output.append(item)

    step(items, depth)

    return output
