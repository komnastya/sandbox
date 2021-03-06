from typing import List

NOTHING = object()  # A special value which denotes absence of item.


# An iterator class which supports the `has_next` method
# which indicates whether there are more items in the iterator.
class HasNextIterator:
    def __init__(self, iterator: List):
        self._iterator = iterator
        self._get_next()

    def _get_next(self):
        try:
            self._next = next(self._iterator)
        except StopIteration:
            self._next = NOTHING

    def has_next(self):
        return self._next is not NOTHING

    def __iter__(self):
        return self

    def __next__(self):
        if self._next is not NOTHING:
            result = self._next
            self._get_next()
            return result
        else:
            raise StopIteration
