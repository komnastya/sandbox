class DictItems():
  def __init__(self, dictionary):
    self.items = []
    for bucket in dictionary.buckets:
      if bucket is not None:
        for key, value in bucket:
          self.items.append((key, value))

  def __str__(self):
            return (
            "dict_items["
            + ", ".join(
                (
                    ('(' + str(key) + ", " + str(value) + ')')
                    for key, value in self.items
                )
            )
            + "]"
        )
