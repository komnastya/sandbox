from typing import List, Optional, Any


# Given a list of lists of lists of items (of arbitrary depth)
# this function returns a single flat list of items.
def flatten_list(items: List[Any], depth: int = 1000) -> List[Any]:
    output = []
    for item in items:
        if isinstance(item, list) and depth > 0:
            output.extend(flatten_list(item, depth - 1))
        else:
            output.append(item)
    return output


def flatten_list2(items: List, depth: Optional[int] = None) -> List[Any]:
    output = []

    def step(items, depth):
        for item in items:
            if isinstance(item, list) and (depth is None or depth > 0):
                step(item, None if depth is None else depth - 1)
            else:
                output.append(item)

    step(items, depth)
    return output
