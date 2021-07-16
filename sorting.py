def bubble_sort(list):
    for j in range(len(list) - 1):
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                current = list[i]
                list[i] = list[i + 1]
                list[i + 1] = current
    return list


def select_sort(list):
    for j in range(len(list)):
        for i in range(j + 1, len(list)):
            if list[i] < list[j]:
                current = list[j]
                list[j] = list[i]
                list[i] = current
    return list
