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
