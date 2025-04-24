def is_weekend(day: int) -> bool:
    return day in {6, 7}


def get_discount(amount: float) -> int:
    return amount / 10 if amount >= 5000 else amount / 20 \
        if amount >= 1000 else 0


def describe_number(numby: int) -> str:
    digits = 1 if numby < 10 else 2 if numby < 100 else 3
    result = 'однозначное' if digits == 1 else 'двузначное' \
        if digits == 2 else 'трехзначное'
    return f'{"четное" if numby % 2 == 0 else "нечетное"} {result} число'


def convert_to_meters(unit: int, numby: float | int) -> float | int:
    match unit:
        case 1:
            return numby * 0.1
        case 2:
            return numby * 1000
        case 3:
            return numby * 1
        case 4:
            return numby * 0.001
        case _:
            return numby * 0.01


def describe_age(age: int) -> str:
    ...