class MyDictKeys:
    """My class for dictionary keys"""

    def __init__(self, owner):
        self.owner = owner

    def __str__(self):
        return (
                "dict_keys["
                + ", ".join(
            (
                str(key)
                for bucket in self.owner.buckets
                if bucket is not None
                for key, value in bucket
            )
        )
                + "]"
        )

    def __len__(self):
        return len(self.owner)

    def __contains__(self, key):
        return key in self.owner

    def __iter__(self):
        for bucket in self.buckets:
            if bucket is not None:
                for pair in bucket:
                    yield pair[0]
