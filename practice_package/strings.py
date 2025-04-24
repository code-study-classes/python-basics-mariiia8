# Задача 1 - L
def extract_file_name(full_file_name):
    normalized_path = full_file_name.replace('\\', '/')
    filename = normalized_path.split('/')[-1]
    parts = filename.split('.')
    if len(parts) == 1 or (len(parts) > 1 and filename.startswith('.')):
        return filename
    return '.'.join(parts[:-1])


# Задача 2
def encrypt_sentence(sentence):
    even_chars = []
    odd_chars = []
    for i, char in enumerate(sentence):
        if i % 2 == 1:
            even_chars.append(char)
        else:
            odd_chars.append(char)
    return ''.join(even_chars) + ''.join(reversed(odd_chars))

 # Задача 3 - Проверка скобок (соответствует тестам)


def check_brackets(expression):
    stack = []
    for pos, char in enumerate(expression):  
        if char == '(':
            stack.append(pos)
        elif char == ')':
            if not stack:
                return pos + 1  
            stack.pop()
    return -1 if stack else 0


# Задача 4
def reverse_domain(domain):
    parts = domain.split('.')
    return '.'.join(reversed(parts))


# Задача 5 - Подсчет групп гласных (соответствует всем тестам)
def count_vowel_groups(word):
   
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'} if 'y' in word.lower() else {'a', 'e', 'i', 'o', 'u'}
    count = 0
    in_group = False
    
    for char in word.lower():
        if char in vowels:
            if not in_group:
                count += 1
                in_group = True
        else:
            in_group = False
    return count