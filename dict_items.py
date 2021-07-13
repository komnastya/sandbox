class DictItems():
  def __init__(self, dictionary):
    self.items = []
    for bucket in dictionary.buckets:
      if bucket is not None:
        for item in bucket:
          self.items.append(item)

  def __str__(self):
            return (
            "dict_items["
            + ", ".join(
                (
                    str(item)
                    for item in self.items
                )
            )
            + "]"
        )
