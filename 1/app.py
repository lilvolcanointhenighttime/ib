from random import choice
from string import digits
import timeit


def generate_password(user_id: str):    
    enlish_alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    special_symbols_list = ['!', '”', '#', '$', '%', '&', '’', '(', ')', '*']
    
    q = len(str(user_id)) % 5
    
    password = ''
    for i in range(0, 10):
        if i <= q:
            password += choice(special_symbols_list)
        if i < 8 and i > q:
            password += choice(enlish_alphabet_list)
        if i == 8:
            password += choice(digits)
    
    return password


def main():
    user_id = str(input('Enter user_id: '))
    print(generate_password(user_id))

if __name__ == '__main__':
    main()