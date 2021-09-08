from typing import List


def count_leaf_items_recursive(item_list: List) -> int:
    """Recursively counts and returns the
    number of leaf items in a (potentially
    nested) list.
    """
    count = 0
    for item in item_list:
        if isinstance(item, list):
            count += count_leaf_items_recursive(item)
        else:
            count += 1

    return count


def count_leaf_items(item_list: List) -> int:
    """Non-recursively counts and returns the
    number of leaf items in a (potentially
    nested) list.
    """
    count = 0
    stack: List = []
    current_list = item_list
    i = 0

    while True:
        if i == len(current_list):
            if current_list == item_list:
                return count
            else:
                current_list, i = stack.pop()
                i += 1
                continue

        if isinstance(current_list[i], list):
            stack.append([current_list, i])
            current_list = current_list[i]
            i = 0
        else:
            count += 1
            i += 1
