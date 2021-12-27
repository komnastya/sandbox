from __future__ import annotations

from typing import Iterator


# making iterators the hard way
class MyRange:
    def __init__(self, start: int, end: int) -> None:
        self.value = start
        self.end = end

    def __iter__(self) -> MyRange:
        return self

    def __next__(self) -> int:
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


# making iterators the easy way
def my_range(start: int, end: int) -> Iterator[int]:
    while start < end:
        yield start
        start += 1
