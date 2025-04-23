check_between_numbers = lambda a, b, c: a < b < c

check_odd_three = lambda numby: numby % 2 == 1 and 100 <= abs(numby) <= 999

check_unique_digits = lambda numby: len(set(str(numby))) == len(str(numby))

def check_palindrome_number(numby: int) -> bool:
    return str(numby) == str(numby)[::-1]

check_ascending_digits = lambda numby: all(numby[i] < numby[i + 1] for i in range(len(numby) - 1)) and len(str(numby)) > 2