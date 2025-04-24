def find_common_elements(set1: set, set2: set) -> set:
    return set1 & set2


def is_superset(set_a: set, set_b: set) -> bool:
    return set_a | set_b == set_a


def remove_duplicates(items: list) -> list:
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result


def count_unique_words(text: str) -> int:
    return len(set(text.lower().split()))


def find_shared_items(*sets: set) -> set:
    return set.intersection(*sets)