from math import log
from random import choice
def password_generator(P: float, V: int, T: int, alphabet):
    A = len(alphabet)

    Slow = round(V*T/P, 1)

    L = round(log(Slow, A))

    password = ''
    for i in range(L):
        password += choice(alphabet)
    return password

def main():
    P = 10**-4
    V = 15
    T = 20160
    enlish_alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    password = password_generator(P, V, T, enlish_alphabet_list)
    print(password)
if __name__ == '__main__':
    main()

