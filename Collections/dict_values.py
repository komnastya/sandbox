class MyDictValues:
    """My class for dictionary values"""

    def __init__(self, owner):
        self.owner = owner

    def __str__(self):
        return (
                "dict_values["
                + ", ".join(
            (
                str(value)
                for bucket in self.owner.buckets
                if bucket is not None
                for key, value in bucket
            )
        )
                + "]"
        )

    def __len__(self):
        return len(self.owner)

    def __iter__(self):
        for bucket in self.owner.buckets:
            if bucket is not None:
                for pair in bucket:
                    yield pair[1]

    def __contain__(self, value):
        for bucket in self.owner.buckets:
            if bucket is not None:
                for b_key, b_value in bucket:
                    if b_value == value:
                        return True
        return False
