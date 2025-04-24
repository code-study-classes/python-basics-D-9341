from typing import Literal


def extract_file_name(path):
    return path.split('/')[-1].split('.')[0]


def encrypt_sentence(sentence: str) -> str:
    even = []
    odd = []
    for i in range(len(sentence)):
        if i % 2 == 0:
            even.append(sentence[i])
        else:
            odd.append(sentence[i])
    return ''.join(odd) + ''.join(even)[::-1]


def check_brackets(string: str) -> Literal[0, 'position', -1]:
    ...


def reverse_domain(domain: str) -> str:
    return '.'.join(domain.split('.')[::-1])


def count_vowel_groups(word: str) -> int:
    vowels = 'aeiouy'
    return len([i for i in word if i.lower() in vowels])