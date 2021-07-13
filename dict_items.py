class MyDictItems():
    def __init__(self, owner):
        self.owner = owner

    def __str__(self):
        return (
            "dict_items["
            + ", ".join(
                ('(' +
                    str(key) + ", " + str(value) + ')'
                    for bucket in self.owner.buckets if bucket is not None
                    for key, value in bucket
                )
            )
            + "]"
        )
