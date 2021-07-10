class MyDict:
    def __init__(self, other=None, capacity=100):
        self.buckets = [None] * capacity
        self.len = 0

    def clear(self):
        for i in range(len(self.buckets)):
            self.buckets[i] = None
        self.len = 0

    def set(self, key, value):
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        print(bucket)
        if bucket is None:
            bucket = [(key, value)]
            self.buckets[index] = bucket
        for pair in bucket:
            keys = [pair[0] for pair in bucket]
        if key not in keys:
            bucket.append((key, value))
        self.len += 1

    def get(self, key, defaults=None):
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        if bucket is not None:
            for pair in bucket:
                keys = [pair[0] for pair in bucket]
            if key in keys:
                for pair in bucket:
                    if pair[0] == key:
                        defaults = pair[1]
        return defaults

    def __len__(self):
        return self.len

    def __contains__(self, key):
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        if bucket is not None:
            keys = [pair[0] for pair in bucket]
            return key in keys
        return False

    def _bucket_index(self, key):
        return abs(hash(key)) % len(self.buckets)

    def __str__(self):
        buckets = [bucket for bucket in self.buckets if bucket is not None]
        return (
            "{"
            + ", ".join(
                (
                    str(pair[0]) + " : " + str(pair[1])
                    for bucket in buckets
                    for pair in bucket
                )
            )
            + "}"
        )
