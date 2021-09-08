# Recursion tasks

# In any of the functions below, using loops `for` and `while` is forbidden!
# The only string operations you are allowed to use are string slicing and concatenation.

# Easy problems
# -------------

# 1. Write a function using recursion to print numbers from n to 0. This function does not return anything, it only prints numbers.

#   def print_numbers_dec(x): pass
#   # print_numbers_dec(3)
#   # 3
#   # 2
#   # 1
#   # 0
from typing import List


def print_numbers_dec(x: int) -> None:
    print(x)
    if x > 0:
        print_numbers_dec(x - 1)


# 2. Write a function using recursion to print numbers from 0 to n. This function does not return anything, it only prints numbers.

#   def print_numbers_inc(x): pass
#   # print_numbers_inc(3)
#   # 0
#   # 1
#   # 2
#   # 3


def print_numbers_inc(x: int) -> None:
    if x > 0:
        print_numbers_inc(x - 1)
    print(x)


# 3. Write a function using recursion to print numbers from n to 0 back to n. This function does not return anything, it only prints numbers.

#   def print_numbers(x): pass
#   # print_numbers(3)
#   # 3
#   # 2
#   # 1
#   # 0
#   # 1
#   # 2
#   # 3


def print_numbers(x: int) -> None:
    print(x)
    if x > 0:
        print_numbers(x - 1)
        print(x)


# 4. Write a function using recursion to return a list of numbers from n to 0. This function does not print anything, it only returns a list of numbers.

#   def numbers_dec(x): pass
#   # numbers_dec(0) -> [0]
#   # numbers_dec(3) -> [3,2,1,0]


def numbers_dec(x: int) -> List:
    output = []
    output.append(x)
    if x > 0:
        output.extend(numbers_dec(x - 1))
    return output


# 5. Write a function using recursion to return a list of numbers from 0 to n. This function does not print anything, it only returns a list of numbers.

#   def numbers_inc(x): pass
#   # numbers_inc(0) -> [0]
#   # numbers_inc(3) -> [0,1,2,3]


def numbers_inc(x: int) -> List:
    output = []
    if x > 0:
        output.extend(numbers_inc(x - 1))
    output.append(x)
    return output


# 6. Write a function using recursion to update a given list with numbers from n to 0. This function does not print or return anything, it updates a list given in an argument.

#   def fill_numbers_dec(x, accum): pass # accum is the list to be updated with numbers
#   # accum = []
#   # fill_numbers_dec(3, accum)
#   # print(accum) -> [3, 2, 1, 0]


def fill_numbers_dec(x: int, accum: List) -> None:
    accum.append(x)
    if x > 0:
        fill_numbers_dec(x - 1, accum)


# 7. Write a function using recursion to update a given list with numbers from 0 to n. This function does not print or return anything, it updates a list given in an argument.

#   def fill_numbers_inc(x, accum): pass # accum is the list to be updated with numbers
#   # accum = []
#   # fill_numbers_int(3, accum)
#   # print(accum) -> [0, 1, 2, 3]


def fill_numbers_inc(
    x: int, accum: List
) -> None:  # accum is the list to be updated with numbers
    if x > 0:
        fill_numbers_inc(x - 1, accum)
    accum.append(x)


# 8. Write a function that takes in two numbers and recursively multiplies them together. Using the `*` operator is forbidden!

#   def mul(a, b): pass
#   # mul(2, 0) -> 0
#   # mul(2, 1) -> 2
#   # mul(2, 3) -> 6


def mul(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return a + mul(a, b - 1)


# 9. Write a function that takes in two numbers `base` and an `exp` and recursively computes `base` ** `exp`. Using the `**` operator is forbidden!

#   def pow(base, exp): pass
#   # pow(2, 0) -> 1
#   # pow(2, 1) -> 2
#   # pow(2, 3) -> 8


def pow(base: int, exp: int) -> int:
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base * pow(base, exp - 1)


# 10. Write a recursive function that takes in one argument n and computes F(n), the n_th value of the Fibonacci sequence. Recall that the Fibonacci sequence is defined by the relation

#   F(n) = F(n−1) + F(n−2)

# where

#   F(0) = 0 and
#   F(1) = 1

#   def fib(n): pass
#   # fib(0) -> 0
#   # fib(1) -> 1
#   # fib(3) -> 2


def fib(n: int) -> int:
    if n == 0:
        return n
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


# 11. Write a recursive implementation of the factorial function. Recall that n! = 1 × 2 × ... × n, with the special case that 0! = 1.

#   def factorial(n): pass
#   # factorial(0) -> 1
#   # factorial(3) -> 6


def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# 12. Write a function using recursion that takes in a string and returns a reversed copy of the string.

#   def reverse(s): pass
#   # reverse("") -> ""
#   # reverse("abc") -> "cba"


def reverse(s: str) -> str:
    if len(s) <= 1:
        return s
    return reverse(s[1:]) + s[0]


# 13. Write a recursive function that checks whether a string is a palindrome (a palindrome is a string that's the same when reads forwards and backwards.)

#   def is_palindrome(s): pass
#   # is_palindrome("madam") -> True
#   # is_palindrome("omg") -> False
#   # is_palindrome("") -> ? Tell me, what is the right answer? True


def is_palindrome(s: str) -> bool:
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])


# Medium problems
# ---------------

# 14. Write a recursive function which counts items in a list, given that the list may contain nested sub-lists, those sub lists also can contain sub-lists, and so on.
#     If any list element is not a sub-list, it is counted as a single item.
#     Unlike in previous excercises, you are allowed to use any statements and operators, including loops `for`, `while`.

#   def item_count(l): pass
#   # item_count([]) -> 0 # empty list
#   # item_count([1, 1, 1]) -> 3 # non-empty flat list without nesting
#   # item_count([[], [[]], [[][]]]) -> 0 # many nested empty sub-lists
#   # item_count([1, [1, [1]]]) -> 3 # many nested non-empty sub-lists


def item_count(l: List) -> int:
    count = 0
    for item in l:
        if isinstance(item, list):
            count += item_count(item)
        else:
            count += 1
    return count


# Hard problems
# -------------

# 15. Write a function, which returns all subsets of a given list of unique elements (generates power set).

#   def power_set(s): pass
#   # power_set([1, 2, 3]) -> [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
