from ranges import MyRange


class MySet:
    def __init__(self, capacity=100):
        self.buckets = [None] * capacity
        self.len = 0

    def add(self, elem):
        index = self._bucket_index(elem)
        bucket = self.buckets[index]
        if bucket is None:
            bucket = []
            self.buckets[index] = bucket
        if elem not in bucket:
            bucket.append(elem)
            self.len += 1

    def delete(self, elem):
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

    def has(self, elem):
        index = self._bucket_index(elem)
        bucket = self.buckets[index]
        return bucket is not None and elem in bucket

    def _bucket_index(self, elem):
        return abs(hash(elem)) % len(self.buckets)

    def __or__(self, other):
        return self.union(other)

    def union(self, other):
        result = MySet()
        for elem in self:
            result.add(elem)
        for elem in other:
            result.add(elem)
        return result

    def intersection(self, other):
        result = MySet()
        for elem in self:
            if elem in other:
                result.add(elem)
        return result

    def __and__(self, other):
        return self.intersection(other)

    def difference(self, other):
        result = MySet()
        for elem in self:
            if elem not in other:
                result.add(elem)
        return result

    def __sub__(self, other):
        return self.difference(other)

    def symmetric_diff(self, other):
        result = MySet()
        for elem in self:
            if elem not in other:
                result.add(elem)
        for elem in other:
            if elem not in self:
                result.add(elem)
        return result

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
