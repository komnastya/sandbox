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

    def step(shifted_array):
        if len(shifted_array) == len(array):
            print(shifted_array)
        else:
            for item in array:
                if item not in shifted_array:
                    shifted_array.append(item)
                    step(shifted_array)
                    shifted_array.pop()

    step(shifted_array)
