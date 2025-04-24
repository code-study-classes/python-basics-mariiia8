
def check_between_numbers(A, B, C):
    return (A < B < C) or (C < B < A)


def check_odd_three(number):
    return (100 <= abs(number) <= 999) and (number % 2 != 0)


def check_unique_digits(number):
    if not (100 <= abs(number) <= 999):
        return False
    num_str = str(abs(number))
    return len(set(num_str)) == 3


def check_palindrome_number(number):
    num_str = str(abs(number))
    return num_str == num_str[::-1]


def check_ascending_digits(number):
    if not (100 <= abs(number) <= 999):
        return False
    digits = [int(d) for d in str(abs(number))]
    return digits[0] < digits[1] < digits[2]