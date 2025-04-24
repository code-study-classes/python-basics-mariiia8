
def square_odds(numbers):
    return [x**2 for x in numbers if x % 2 != 0]


def normalize_names(names):
    return [name.capitalize() for name in names]


def remove_invalid_emails(emails):
    valid_emails = []
    for email in emails:
        if email.count('@') != 1:
            continue
        if len(email) < 5:
            continue
        if email.startswith('@') or email.endswith('@'):
            continue
        valid_emails.append(email)
    return valid_emails


def filter_palindromes(words):
    return [word for word in words if word.lower() == word.lower()[::-1]]


def calculate_factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def find_common_prefix(strings):
    if not strings:
        return ""
    
    prefix = strings[0]
    for string in strings[1:]:
        while string[:len(prefix)] != prefix and prefix:
            prefix = prefix[:-1]
            if not prefix:
                break
    return prefix