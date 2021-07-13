from dict_items import MyDictItems
from dict_keys import MyDictKeys
from dict_values import MyDictValues

class MyDict:
    def __init__(self, other=None, capacity=100):
        self.buckets = [None] * capacity
        self.len = 0

    def clear(self):
        for i in range(len(self.buckets)):
            self.buckets[i] = None
        self.len = 0

    def copy(self):
        result = MyDict()
        for bucket in self.buckets:
            if bucket is not None:
                for key, value in bucket:
                    result[key] = value
        return result

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
        if bucket is not None:
            key_index = find_key_index(bucket, key)
            if key_index != -1:
                return bucket[key_index][1]
        raise KeyError

    def __delitem__(self, key):
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        key_index = find_key_index(bucket, key)
        if key_index != -1:
            del bucket[key_index]
            self.len -= 1
        else:
            raise KeyError

    def pop(self, key, default=None):
        try:
            default = self[key]
            del self[key]
            return default
        except KeyError:
            if default is not None:
                return default
            else:
                raise KeyError

    def setdefault(self, key, default=None):
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        if bucket is not None:
            key_index = find_key_index(bucket, key)
            if key_index != -1:
                return bucket[key_index][1]
            if default is not None:
                self[key] = default
                return self[key]
        return default

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
        return (
            "{"
            + ", ".join(
                (
                    (str(key) + ": " + str(value))
                    for bucket in self.buckets
                    if bucket is not None
                    for key, value in bucket
                )
            )
            + "}"
        )

    # Returns a new dictionary with keys from seq and value equal to v (defaults to None).
    def fromkeys(self, seq, v=None):
        result = MyDict()
        for key in seq:
            result[key] = v
        return result

    # Return a new object of the dictionary's items in (key, value) format.
    def items(self):
        return MyDictItems(self)

    def keys(self):
        return MyDictKeys(self)

    def values(self):
        return MyDictValues(self)


def find_key_index(bucket, key):
    for i in range(len(bucket)):
        if bucket[i][0] == key:
            return i
    return -1
