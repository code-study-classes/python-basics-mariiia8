# Задача 1: Сумма четных цифр
def sum_even_digits(number):
    return sum(int(digit) for digit in str(abs(number)) if int(digit) % 2 == 0)


# Задача 2: Количество троек подряд идущих гласных
def count_vowel_triplets(text):
    vowels = "aeiouy"  
    text = text.lower()
    count = 0
    i = 0

    while i < len(text) - 2:
        if text[i] in vowels and text[i + 1] in vowels and text[i + 2] in vowels:
            count += 1
            i += 3
        else:
            i += 1

    return count


# Задача 3: Индекс числа в последовательности Фибоначчи
def find_fibonacci_index(number):
    if number == 0:
        return -1
    a, b = 0, 1
    index = 1
    while b < number:
        a, b = b, a + b
        index += 1
    return index if b == number else -1


# Задача 4: Удаление подряд идущих дубликатов
def remove_duplicates(string):
    if not string:
        return ""
    result = [string[0]]
    for char in string[1:]:
        if char != result[-1]:
            result.append(char)
    return ''.join(result)
