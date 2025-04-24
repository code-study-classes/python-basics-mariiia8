# Задача 1 - L
def extract_file_name(full_file_name):
    filename = full_file_name.replace('\\', '/').split('/')[-1]
    return filename.rsplit('.', 1)[0] if '.' in filename else filename

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

# Задача 3
def check_brackets(expression):
    stack = []
    for i, char in enumerate(expression):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if not stack:
                return i
            stack.pop()
    return -1 if stack else 0

# Задача 4
def reverse_domain(domain):
    parts = domain.split('.')
    return '.'.join(reversed(parts))

# Задача 5
def count_vowel_groups(word):
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    count = 0
    in_vowel_group = False
    for char in word.lower():
        if char in vowels:
            if not in_vowel_group:
                count += 1
                in_vowel_group = True
        else:
            in_vowel_group = False
    return count