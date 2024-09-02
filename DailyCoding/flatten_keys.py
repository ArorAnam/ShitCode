
# Time Complexity: O(n)
# Space Complexity: O(n)
# Recursion Stack: O(D), where D is the maximum depth of the nested dictionary
def flatten_dict(d, parent_key=''):
    items = {}
    for k, v in d.items():
        new_key = f'{parent_key}.{k}' if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key))
        else:
            items[new_key] = v
    return items

# Example usage:
nested_dict = {
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}

flattened_dict = flatten_dict(nested_dict)
print(flattened_dict)