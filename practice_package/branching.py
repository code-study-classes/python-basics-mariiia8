
def is_weekend(day):
    return day == 6 or day == 7


def get_discount(amount):
    if amount >= 5000:
        return round(amount * 0.10, 2)
    elif amount >= 1000:
        return round(amount * 0.05, 2)
    else:
        return 0.0


def describe_number(n):
    parity = "четное" if n % 2 == 0 else "нечетное"
    
    abs_n = abs(n)
    if 0 <= abs_n <= 9:
        digit = "однозначное"
    elif 10 <= abs_n <= 99:
        digit = "двузначное"
    else:
        digit = "трехзначное"
    
    return f"{parity} {digit} число"


def convert_to_meters(unitNumber, lengthInUnits):
    conversion = {
        1: 0.1,    # дециметр
        2: 1000,    # километр
        3: 1,       # метр
        4: 0.001,   # миллиметр
        5: 0.01     # сантиметр
    }
    return lengthInUnits * conversion.get(unitNumber, 0)


def describe_age(age):
    tens = {
        2: "двадцать",
        3: "тридцать",
        4: "сорок",
        5: "пятьдесят",
        6: "шестьдесят",
        7: "семьдесят",
        8: "восемьдесят",
        9: "девяносто",
        10: "сто"
    }
    
    units = {
        1: "один",
        2: "два",
        3: "три",
        4: "четыре",
        5: "пять",
        6: "шесть",
        7: "семь",
        8: "восемь",
        9: "девять"
    }
    
    if age % 10 == 0 or age in [11, 12, 13, 14]:
        word = tens[age // 10] + " лет"
    elif 5 <= age % 10 <= 9 or age % 10 == 0:
        word = tens[age // 10] + " " + units[age % 10] + " лет"
    elif 2 <= age % 10 <= 4:
        word = tens[age // 10] + " " + units[age % 10] + " года"
    else:  # 1
        word = tens[age // 10] + " " + units[age % 10] + " год"
    
    return word