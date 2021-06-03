class PushBackIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.added_elements = []

    def __iter__(self):
        return self

    def __next__(self):
        while self.added_elements:
            return self.added_elements.pop()
        return next(self.iterator)

    def push_back(self, element):
        self.added_elements.append(element)
