# A function which prints all permutations of a given list of unique elements.
# Example:
# permutations([1, 2, 3]):
# [1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 2, 1]
# [3, 1, 2]


def permutations(array):
    shifted_array = []

    def step():
        if len(shifted_array) == len(array):
            print(shifted_array)
        else:
            for item in array:
                if item not in shifted_array:
                    shifted_array.append(item)
                    step(shifted_array)
                    shifted_array.pop()

    step()


def permutations2(l, pos=0):
    if pos == len(l):
        print(l)
    else:
        for i in range(pos, len(l)):
            l[pos], l[i] = l[i], l[pos]
            permutations2(l, pos + 1)
            l[pos], l[i] = l[i], l[pos]


def permutations_gen(l, pos=0):
    if pos == len(l):
        yield l
    else:
        for i in range(pos, len(l)):
            l[pos], l[i] = l[i], l[pos]
            yield from permutations_gen(l, pos + 1)
            l[pos], l[i] = l[i], l[pos]
