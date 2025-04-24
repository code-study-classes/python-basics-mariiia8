# Задача 1
def count_char_occurrences(text):
    result = {}
    for char in text.lower():
        if char.isalpha() and char != '-':  
            result[char] = result.get(char, 0) + 1
    return result


# Задача 2
def merge_dicts(dict1, dict2, conflict_resolver):
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            merged[key] = conflict_resolver(key, merged[key], value)
        else:
            merged[key] = value
    return merged


# Задача 3
def invert_dictionary(original_dict):
    inverted = {}
    for key, value in original_dict.items():
        if value in inverted:
            if isinstance(inverted[value], list):
                inverted[value].append(key)
            else:
                inverted[value] = [inverted[value], key]
        else:
            inverted[value] = [key]
    return inverted


# Задача 4
def dict_to_table(data_dict, columns):
    if not data_dict or not columns:
        return ""
    
    headers = [col.upper() for col in columns]
    rows = []
    max_lengths = [len(header) for header in headers]
    
    for item in data_dict.values():
        row = []
        for i, col in enumerate(columns):
            value = str(item.get(col, "N/A"))
            row.append(value)
            max_lengths[i] = max(max_lengths[i], len(value))
        rows.append(row)
    
    header_line = "| " + " | ".join(
        header.ljust(length) for header, length in zip(headers, max_lengths)
    ) + " |"
    separator_line = "|-" + "-|-".join(
        "-" * length for length in max_lengths
    ) + "-|"
    data_lines = [
        "| " + " | ".join(
            value.ljust(length) for value, length in zip(row, max_lengths)
        ) + " |"
        for row in rows
    ]
    
    return "\n".join([header_line, separator_line] + data_lines)


# Задача 5
def deep_update(base_dict, update_dict):
    result = base_dict.copy()
    for key, value in update_dict.items():
        if key in result:
            if isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = deep_update(result[key], value)
            else:
                result[key] = value
        
    return result