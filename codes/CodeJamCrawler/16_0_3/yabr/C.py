def func(N, J):
    produced = 0
    stringNumber = 0

    while produced < J:
        noPrime = True
        dividers = []

        string = '1' + bin(stringNumber)[2:].zfill(N-2) + '1'

        for base in range(2, 11):
            if isPrime(convertBase(string, base), dividers):
                noPrime = False
                break

        if noPrime:
            print(string + ' ' + ' '.join(str(div) for div in dividers))
            produced += 1

        stringNumber += 1


def isPrime(n, dividers):
    # See https://en.wikipedia.org/wiki/Primality_test#Pseudocode

    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        dividers.append(2)
        return False
    if n % 3 == 0:
        dividers.append(3)
        return False

    i = 5

    while i * i <= n:
        if n % i == 0:
            dividers.append(i)
            return False
        if n % (i + 2) == 0:
            dividers.append(i+2)
            return False
        i += 6

    return True


def convertBase(string, base):
    number = 0

    for i in range(len(string)):
        number += int(string[i]) * (base ** (len(string) - i - 1))

    return number

T = int(input())

N, J = input().split(' ')
print('Case #' + str(T) + ':')
func(int(N), int(J))

