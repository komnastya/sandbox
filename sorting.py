def bubble_sort(list):
    for j in range(len(list)):
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
    return list


def select_sort(list):
    for j in range(len(list)):
        for i in range(j + 1, len(list)):
            if list[i] < list[j]:
                list[i], list[j] = list[j], list[i]
    return list


def insert_sort(list):
    for i in range(1, len(list)):
        for j in range(0, i):
            if list[i] < list[j]:
                list.insert(j, list.pop(i))
    return list


def quick_sort(arr):
    def portition(arr, l, r):
        pivot = arr[r]
        i = l - 1
        for j in range(l, r):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[r] = arr[r], arr[i + 1]
        return i + 1

    def qs(arr, l, r):
        if l >= r:
            return
        p = portition(arr, l, r)

        qs(arr, l, p - 1)
        qs(arr, p + 1, r)

    qs(arr, 0, len(arr) - 1)

    return arr
