import random
import string


def line(txt):
    print('-' * len(txt))
    print(txt)
    print('-' * len(txt))


def generate_password(length, upper=True, lower=True, numbers=True, symbols=True):
    all_chars = ''
    if upper:
        all_chars += string.ascii_uppercase
    if lower:
        all_chars += string.ascii_lowercase
    if numbers:
        all_chars += string.digits
    if symbols:
        all_chars += '#$@!%¨&*()[]{}^?:><-+=/'

    if not all_chars:
        raise ValueError('You must select at least one option!')

    return ''.join(random.choices(all_chars, k=length))
