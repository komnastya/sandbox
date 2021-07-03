class MySet:
    def __init__(self, other=None, capacity=100):
        self.buckets = [None] * capacity
        self.len = 0
        if other is not None:
            for elem in other:
                self.add(elem)

    def clear(self):
        for i in range(len(self.buckets)):
            self.buckets[i] = None
        self.len = 0

    def copy(self):
        result = MySet()
        for elem in self:
            result.add(elem)
        return result

    def add(self, elem):
        index = self._bucket_index(elem)
        bucket = self.buckets[index]
        if bucket is None:
            bucket = []
            self.buckets[index] = bucket
        if elem not in bucket:
            bucket.append(elem)
            self.len += 1

    def discard(self, elem):
        index = self._bucket_index(elem)
        bucket = self.buckets[index]
        if bucket is not None:
            try:
                bucket.remove(elem)
                self.len -= 1
            except ValueError:
                pass
            if not bucket:
                self.buckets[index] = None

    def remove(self, elem):
        index = self._bucket_index(elem)
        bucket = self.buckets[index]
        if bucket is None or elem not in bucket:
            raise KeyError
        if bucket is not None:
            bucket.remove(elem)
            self.len -= 1
        if not bucket:
            self.buckets[index] = None

    def pop(self):
        for i in range(len(self.buckets)):
            bucket = self.buckets[i]
            if bucket is not None:
                elem = bucket.pop()
                self.len -= 1
                if not bucket:
                    self.buckets[i] = None
                return elem
        raise KeyError

    def has(self, elem):
        index = self._bucket_index(elem)
        bucket = self.buckets[index]
        return bucket is not None and elem in bucket

    def _bucket_index(self, elem):
        return abs(hash(elem)) % len(self.buckets)

    def union(self, other):
        result = MySet()
        for elem in self:
            result.add(elem)
        for elem in other:
            result.add(elem)
        return result

    def __or__(self, other):
        return self.union(other)

    def update(self, other):
        for elem in other:
            self.add(elem)
        return self

    def __ior__(self, other):
        return self.update(other)

    def intersection(self, other):
        result = MySet()
        for elem in self:
            if elem in other:
                result.add(elem)
        return result

    def __and__(self, other):
        return self.intersection(other)

    def intersection_update(self, other):
        for elem in self:
            if elem not in other:
                self.discard(elem)
        return self

    def __iand__(self, other):
        return self.intersection_update(other)

    def difference(self, other):
        result = MySet()
        for elem in self:
            if elem not in other:
                result.add(elem)
        return result

    def __sub__(self, other):
        return self.difference(other)

    def difference_update(self, other):
        for elem in self:
            if elem in other:
                self.discard(elem)
        return self

    def __isub__(self, other):
        return self.difference_update(other)

    def symmetric_difference(self, other):
        result = MySet()
        for elem in self:
            if elem not in other:
                result.add(elem)
        for elem in other:
            if elem not in self:
                result.add(elem)
        return result

    def __xor__(self, other):
        return self.symmetric_difference(other)

    def __ixor__(self, other):
        for elem in self:
            if elem in other:
                self.discard(elem)
                other.discard(elem)
        for elem in other:
            if elem not in self:
                self.add(elem)
        return self

    def isdisjoint(self, other):
        for elem in self:
            if elem in other:
                return False
        return True

    def issubset(self, other):
        for elem in self:
            if elem not in other:
                return False
        return True

    def issuperset(self, other):
        for elem in other:
            if elem not in self:
                return False
        return True

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) is not type(other):
            return False
        if len(self) != len(other):
            return False
        for elem in self:
            if elem not in other:
                return False
        for elem in other:
            if elem not in self:
                return False
        return True

    def __iter__(self):
        for bucket in self.buckets:
            if bucket is not None:
                yield from bucket

    def __len__(self):
        return self.len

    def __str__(self):
        return "{" + ", ".join((str(elem) for elem in self)) + "}"

    def fill_factor(self):
        return self.len / len(self.buckets)

    def max_bucket_length(self):
        result = 0
        for bucket in self.buckets:
            if bucket is not None:
                result = max(result, len(bucket))
        return result
