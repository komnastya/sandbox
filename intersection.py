def intersect(a, b):
    output = []
    a = sorted(a)
    b = sorted(b)
    ia = 0
    ib = 0
    while ia < len(a) and ib < len(b):
        if a[ia] > b[ib]:
            ib += 1
        elif b[ib] > a[ia]:
            ia += 1
        else:
            output.append(a[ia])
            ia += 1
            ib += 1
    return output
