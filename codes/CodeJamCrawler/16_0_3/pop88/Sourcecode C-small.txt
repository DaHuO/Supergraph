from math import sqrt
def toBaseStr(n, base):
    '''
    convert an int n in dec to any base <= 10
    '''
    convertStr = '0123456789'
    if n < base:
        return convertStr[n]
    return toBaseStr(n//base, base) + convertStr[n%base]

def toDecStr(n, base):
    '''
    convert an int in base to dec
    '''
    res, digits = 0, len(str(n))
    for i in range(digits):
        res += int(str(n)[i]) * (base ** (digits - i - 1))
    return res

def is_not_prime(number):
    '''
    checks if a number is not prime and
    returns a nontrivial divisor
    '''
    for i in range(2, int(sqrt(number)) + 1):
        if not number % i:
            return (True, i)
    return (False, 0)

def is_jamcoin(number):
    for base in range(2,11):
        if not is_not_prime(int(toDecStr(number, base)))[0]:
            return False
    return True

def jamcoins(N,J):
    count, i = 0, 1
    inside = 2 ** (N - 2)
    print('Case #1:')
    while count < J:
        number = 10**(N-1) + int(toBaseStr(i, 2))*10 + 1
        if is_jamcoin(number):
            count += 1
            print(number, end = ' ')
            for base in range(2, 11):
                print(is_not_prime(int(toDecStr(number, base)))[1], end = ' ')
            print('')
        i += 1

jamcoins(16,50)
