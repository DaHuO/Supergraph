import primesieve
from datetime import datetime

THR = 200

def jamcoins(length, count):
    d = {}
    num = [1] + ([0] * (length - 2)) + [1]
    while len(d) < count:
        divisors = get_divisors(num)
        if divisors is not None:
            d[''.join(map(str, num))] = divisors
        num = increment(num)
    return d

def get_divisors(num):
    divs = []
    for base in range(2,11):
        converted = convert(num, base)
        it = primesieve.Iterator()
        prime = it.next_prime()
        while converted % prime != 0 and prime < THR:
            prime = it.next_prime()
        if prime > THR:
            return None
        else:
            divs.append(prime)
    return divs

def convert(num, base):
    output = 0
    exp = 1
    for digit in reversed(num):
        output += digit * exp
        exp *= base
    return output

def increment(num):
    if all(map(lambda x: x == 1, num)):
        raise ValueError('Number cannot be incremented more')
    for i, dig in enumerate(list(reversed(num))[1:]):
        if dig == 0:
            num[len(num) - i - 2] = 1
            return num
        else:
            num[len(num) - i - 2] = 0
    return num


# MAIN
now = datetime.now()
with open('input.txt', 'r') as f:
    for i, line in enumerate(f.readlines()[1:]):
        print('Case #' + str(i+1) + ':')
        length = int(line.split()[0])
        count = int(line.split()[1])
        d = jamcoins(length, count)
        for key in d.keys():
            print(str(key) + ' ' + ' '.join(map(str,d[key])))

