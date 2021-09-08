from typing import List

from merge_lists import merge_lists


def bubble_sort(list: List) -> List:
    for j in range(len(list)):
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
    return list


def select_sort(list: List) -> List:
    for j in range(len(list)):
        for i in range(j + 1, len(list)):
            if list[i] < list[j]:
                list[i], list[j] = list[j], list[i]
    return list


def insert_sort(list: List) -> List:
    for i in range(1, len(list)):
        for j in range(0, i):
            if list[i] < list[j]:
                list.insert(j, list.pop(i))
    return list


def quick_sort(arr: List) -> List:
    def portition(l, r):
        pivot = arr[r]
        i = l - 1
        for j in range(l, r):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[r] = arr[r], arr[i + 1]
        return i + 1

    def qs(l, r):
        if l >= r:
            return
        p = portition(l, r)

        qs(l, p - 1)
        qs(p + 1, r)

    qs(0, len(arr) - 1)

    return arr


def merge_sort(arr: List) -> List:
    if len(arr) > 1:

        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr


# Merge sorting using merge_lists function


def merge_sort_2(arr: List) -> List:
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        return merge_lists(merge_sort_2(left), merge_sort_2(right))
