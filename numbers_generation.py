from typing import List


# Recursively generates a list of all numbers with the given number of digits.
def numbers0(size: int, digits: List[int]):
    # This function keeps the temporary list of digits in an argument.
    if len(digits) == size:
        print(digits)
    else:
        for d in range(10):
            numbers0(size, [d] + digits)


# Recursively generates a list of all numbers with the given number of digits.
def numbers1(size: int, digits: List[int]):
    # This function keeps the temporary list of digits in an argument.
    if len(digits) == size:
        print(digits)
    else:
        for d in range(10):
            digits.append(d)  # Add a digit to the number.
            numbers1(size, digits)
            digits.pop()  # Remove the digit.


# Recursively generates a list of all numbers with the given number of digits.
def numbers2(size: List[int]):
    # This function keeps the temporary list of digits in a local variable.

    digits: List = []

    def step():
        if len(digits) == size:
            print(digits)
        else:
            for d in range(10):
                digits.append(d)
                step()  # A recursive call.
                digits.pop()

    step()  # The initial call.
