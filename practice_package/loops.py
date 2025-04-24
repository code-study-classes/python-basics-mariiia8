# Задача 1
def sum_even_digits(number):
    total = 0
    num = abs(number)
    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            total += digit
        num = num // 10
    return total


# Задача 2
def count_vowel_triplets(text):
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    count = 0
    text_lower = text.lower()
    
    for i in range(len(text_lower) - 2):
        if (text_lower[i] in vowels and 
            text_lower[i + 1] in vowels and 
            text_lower[i + 2] in vowels):
            count += 1
    return count


# Задача 3
def find_fibonacci_index(number):
    if number < 1:
        return -1
    if number == 1:
        return 1  
    
    a, b = 1, 1
    index = 2
    while b < number:
        a, b = b, a + b
        index += 1
    
    return index if b == number else -1


# Задача 4
def remove_duplicates(string):
    if not string:
        return ""
    
    result = string[0]
    for char in string[1:]:
        if char != result[-1]:
            result += char
    return result