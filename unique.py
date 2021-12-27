from typing import Iterable, Iterator


# Return unique elements from the sequence
# unique(iter([1,2,1,2]))) -> [1,2]


def unique(it: Iterable[int]) -> Iterator[int]:  # or Generator[int, None, None]
    it = iter(it)
    my_set = set()
    while True:
        try:
            element = next(it)
        except StopIteration:
            break
        if element not in my_set:
            yield element
            my_set.add(element)
