import pickle
import os

from tools.builders.essentials import line, generate_password


def save(passwords):
    with open('passwords.pickle', 'wb') as file:
        pickle.dump(passwords, file)


def load():
    try:
        with open('passwords.pickle', 'rb') as file:
            passwords = pickle.load(file)
    except FileNotFoundError:
        passwords = []
    return passwords


def display_saved(passwords):
    if passwords:
        print('\nSaved Passwords: ')
        for i, password in enumerate(passwords, 1):
            print(f'{i} - {password}')
    else:
        print('No passwords saved yet!')


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    line('PASSWORD GENERATOR')

    try:
        length = int(input('Enter the password length: '))
        amount = int(input('Enter the number of passwords to generate: '))

        if length <= 0 or amount <= 0:
            raise ValueError("Length and amount must be positive integers.")

        enter = input(
            '''Select the options that you want in your password! (default: 1 2 3 4):
            1 - Uppercase Letters
            2 - Lowercase Letters
            3 - Numbers
            4 - Symbols
            Type here:'''
            )

        upper = '1' in enter
        lower = '2' in enter
        numbers = '3' in enter
        symbols = '4' in enter

        passwords = load()

        generated = []

        for i in range(1, amount + 1):
            password = generate_password(length, upper=upper, lower=lower, numbers=numbers, symbols=symbols)
            generated.append(password)
            print(f'Your {i}º password is: {password}')

        passwords.extend(generated)
        save(passwords)

        try:
            show = input('Do you want to see the saved passwords? (y/n)')
            if show.lower() == 'y':
                display_saved(passwords)
        except TypeError as te:
            print(f'Error: {te}')

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
