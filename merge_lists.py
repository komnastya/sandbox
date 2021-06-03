def merge_lists(a, b):
    output = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            output.append(a[i])
            i += 1
        else:
            output.append(b[j])
            j += 1
    output.extend(b[j:])
    output.extend(a[i:])
    return output
