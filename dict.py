class MyDict:
    def __init__(self, other=None, capacity=100):
        self.buckets = [None] * capacity
        self.len = 0

    def clear(self):
        for i in range(len(self.buckets)):
            self.buckets[i] = None
        self.len = 0

    def set(self, key, value):
        self[key] = value

    def __setitem__(self, key, value):
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        if bucket is None:
            bucket = []
            self.buckets[index] = bucket
        key_index = find_key_index(bucket, key)
        if key_index != -1:
            bucket[key_index] = (key, value)
        else:
            bucket.append((key, value))
            self.len += 1

    def get(self, key, defaults=None):
        try:
            return self[key]
        except KeyError:
            return defaults

    def __getitem__(self, key):
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        key_index = find_key_index(bucket, key)
        if key_index != -1:
            return bucket[key_index][1]
        raise KeyError

    def __delitem__(self, key):
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        key_index = find_key_index(bucket, key)
        del bucket[key_index]
        self.len -= 1

    def popitem(self):
        for i in range(len(self.buckets)):
            bucket = self.buckets[i]
            if bucket is not None:
                pair = self.buckets[i].pop()
                self.len -= 1
                if not bucket:
                    self.buckets[i] = None
                return pair
        raise KeyError

    def __len__(self):
        return self.len

    def __contains__(self, key):
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        return bucket is not None and find_key_index(bucket, key) != -1

    def _bucket_index(self, key):
        return abs(hash(key)) % len(self.buckets)

    def __str__(self):
        buckets = (bucket for bucket in self.buckets if bucket is not None)
        return (
            "{"
            + ", ".join(
                (
                    (str(key) + " : " + str(value))
                    for bucket in buckets
                    for key, value in bucket
                )
            )
            + "}"
        )


def find_key_index(bucket, key):
    if bucket is not None:
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                return i
    return -1
