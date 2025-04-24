def sum_even_digits(numby: int) -> int:
    result = 0
    for i in str(abs(numby)):
        if int(i) % 2 == 0:
            result += int(i)
    return result


def count_vowel_triplets(w: str) -> int:
    vowels = 'aeiouy'
    result = 0
    for i in range(len(w) - 2):
        if w[i] in vowels and w[i + 1] in vowels and w[i + 2] in vowels:
            result += 1
    return result


def find_fibonacci_index(numby: int) -> int:
    ...


def remove_duplicates(string: str) -> str:
    ...