from typing import Any, Dict

# Recursively flatten a dictionary of dictionaries.
# The result is a single flat dictionary.
# To avoid collisions in the case of nested dictionaries their keys
# are joined with the parent keys using the dot character "." as a separator.
# For example, the following structure
#
# { "key0": "value0", "key1": { "key1_0": "value1_0" } }
#
# is converted into the following dictionary
#
# { "key0": "value0", "key1.key1_0", "value1_0" }
#                      ^^^^^^^^^^^
#                      Here we joined keys of the containing
#                      and the nested dictionary items.
def flatten_dict(d: Dict[str, Any]) -> Dict[str, Any]:
    output = {}

    def step(d, upper_key=None):
        for key, value in d.items():
            if upper_key is not None:
                key = upper_key + "." + key
            if isinstance(value, dict):
                step(value, key)
            else:
                output[key] = value

    step(d)

    return output
