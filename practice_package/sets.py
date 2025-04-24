# Задача 1
def find_common_elements(set1, set2):
    common = set()
    for item in set1:
        if item in set2:
            common.add(item)
    return common


# Задача 2
def is_superset(set_a, set_b):
    for item in set_b:
        if item not in set_a:
            return False
    return True


# Задача 3
def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


# Задача 4
def count_unique_words(text):
    words = text.lower().split()
    return len(set(words))


# Задача 5
def find_shared_items(*sets):
    if not sets:
        return set()
    
    common = sets[0].copy()
    for s in sets[1:]:
        common.intersection_update(s)
        if not common:
            break
    return common