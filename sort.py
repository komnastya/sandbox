from typing import List


def is_sorted(list: List) -> bool:
    if len(list) == 0:
        return True
    for x in range(len(list) - 1):
        if list[x] > list[x + 1]:
            return False
    return True
