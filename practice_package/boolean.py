def check_between_numbers(a, b, c):
    return (a < b < c) or (a > b > c)


def check_odd_three(numby):
    return numby % 2 == 1 and 100 <= abs(numby) <= 999


def check_unique_digits(numby):
    return len(set(str(numby))) == len(str(numby)) and len(str(abs(numby))) == 3


def check_palindrome_number(numby: int) -> bool:
    return str(abs(numby)) == str(abs(numby))[::-1]


def check_ascending_digits(numby):
    numby = str(abs(numby))
    st = all(numby[i] < numby[i + 1] for i in range(len(numby) - 1))
    return st and len(str(numby)) > 2