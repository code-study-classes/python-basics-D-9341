# списки и так называемые массивы - совершенно разные типы данных

def square_odds(numbies: list[int]) -> list[int]:
    return [numby ** 2 for numby in numbies if numby % 2 != 0]


def normalize_names(names: list[str]) -> list[str]:
    return [name.lower().capitalize() for name in names]


def remove_invalid_emails(emails: list[str]) -> list[str]:
    return [email for email in emails if '@' in email and len(email) > 5 
            and email[0] != '@' and email[-1] != '@' and email.count('@') == 1]


def filter_palindromes(strings: list[str]) -> list[str]:
    return [s for s in strings if s.lower() == s[::-1].lower()]


class memoize:
    """
    A decorator object that memoizes the results of recursive functions
    for multiple times faster execution, consuming more memory.
    """
    def __init__(self, f):
        self.f = f
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]
    

@memoize
def calculate_factorial(n: int) -> int:
    return 1 if n == 0 else n * calculate_factorial(n - 1)


def find_common_prefix(strings: list[str]) -> str:
    ...