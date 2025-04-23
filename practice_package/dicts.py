def count_char_occurrences(text: str) -> dict:
    result = {}
    for i in text.lower():
        if i.isalpha():
            result[i] = result.get(i, 0) + 1
    return result

def merge_dicts(d1: dict, d2: dict, resolver: callable) -> dict:
    result = d1.copy()
    for k, v in d2.items():
        if k in result:
            result[k] = resolver(k, result[k], v)
        else:
            result[k] = v
    return result

def invert_dictionary(d: dict) -> dict:
    return {v: k for k, v in d.items()}

def dict_to_table(data: dict, columns: list) -> str:
    ...

def deep_update(base_dict: dict, update_dict: dict) -> dict:
    ...