# This function keeps the temporary list of digits in an argument.
from typing import List


def numbers0(size: int, digits: List):
    if len(digits) == size:
        print(digits)
    else:
        for d in range(10):
            numbers0(size, [d] + digits)


# This function keeps the temporary list of digits in an argument.
def numbers1(size: int, digits: List):
    if len(digits) == size:
        print(digits)
    else:
        for d in range(10):
            digits.append(d)  # Add a digit to the number.
            numbers1(size, digits)
            digits.pop()  # Remove the digit.


# This function keeps the temporary list of digits in a local variable.
def numbers2(size: List):
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
