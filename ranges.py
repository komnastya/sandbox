class my_range:
    # making iterators the hard way

    def __init__(self, start, end):
        print("my_range.___init__(...)")
        self.value = start
        self.end = end

    def __iter__(self):
        print("my_range.___iter__(...)")
        return self

    def __next__(self):
        print("my_range.___next__(...)")
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


def my_range_2(start, end):
    # making iterators the easy way

    print("my_range_2", start)

    while start < end:
        yield start
        start += 1


for item in my_range(1, 10):
    print("elem=", item, sep="")

for item in my_range_2(1, 10):
    print("elem=", item, sep="")
