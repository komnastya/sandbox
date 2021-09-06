# A function which prints all permutations of a given list of unique elements.
# Example:
# permutations([1, 2, 3]):
# [1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 2, 1]
# [3, 1, 2]
from typing import List


def permutations(items: List) -> None:
    result: List = []

    def step():
        if len(result) == len(items):
            print(result)
        else:
            for item in items:
                if item not in result:
                    result.append(item)
                    step()
                    result.pop()

    step()


def permutations2(items: List, pos: int = 0):
    if pos == len(items):
        print(items)
    else:
        for i in range(pos, len(items)):
            items[pos], items[i] = items[i], items[pos]
            permutations2(items, pos + 1)
            items[pos], items[i] = items[i], items[pos]


def permutations_gen(items, pos=0):
    if pos == len(items):
        yield items
    else:
        for i in range(pos, len(items)):
            items[pos], items[i] = items[i], items[pos]
            yield from permutations_gen(items, pos + 1)
            items[pos], items[i] = items[i], items[pos]
