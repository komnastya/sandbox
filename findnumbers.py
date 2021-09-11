from typing import Generator, List


# Finds all positive integers in the given string.


def find_numbers(s: str) -> List[int]:
    output = []
    i = 0
    while i < len(s):
        try:
            number = int(s[i])
            j = i + 1
            while j < len(s):
                try:
                    next_number = int(s[j])
                    number = number * 10 + next_number
                    j += 1
                except ValueError:
                    break
            output.append(number)
            i = j + 1
        except ValueError:
            i += 1
            continue
    return output


def find_numbers_2(s: str) -> Generator[int, None, None]:
    i = 0
    while i < len(s):
        char = ord(s[i])
        if char >= 48 and char <= 57:
            j = i + 1
            while j < len(s):
                char = ord(s[j])
                if not (char >= 48 and char <= 57):
                    break
                j += 1
            yield int(s[i:j])
            i = j
        i += 1


def find_numbers_sm_bool(s: str) -> Generator[int, None, None]:
    in_number = False  # False means text, True means number
    start = 0
    for i, c in enumerate(s + "\0"):
        char: int = ord(c)
        is_digit: bool = char >= 48 and char <= 57
        if not in_number:
            if is_digit:
                in_number = True
                start = i
        else:
            if not is_digit:
                in_number = False
                yield int(s[start:i])


S_TEXT = 1
S_NUM = 2


def find_numbers_sm(s: str) -> Generator[int, None, None]:
    state = S_TEXT
    start = 0
    for i, c in enumerate(s + "\0"):
        char: int = ord(c)
        is_digit: bool = char >= 48 and char <= 57
        if state == S_TEXT:
            if is_digit:
                state = S_NUM
                start = i
            if not is_digit:
                continue  # change nothing
            continue
        if state == S_NUM:
            if is_digit:
                continue  # change nothing
            if not is_digit:
                state = S_TEXT
                yield int(s[start:i])
            continue
