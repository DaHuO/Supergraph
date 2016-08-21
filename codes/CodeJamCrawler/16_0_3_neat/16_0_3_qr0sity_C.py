import sys
from itertools import islice, product

def make_num(digits, base):
    num = 0
    for digit in digits:
        num = num*base + digit
    return num

def divisor(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: 
            return i
    return num

def base_prime(digits, base):
    num = make_num(digits, base)
    return divisor(num) == num

def jamcoins(bdigits):
    for digits in product((0, 1), repeat=bdigits-2):
        digits = (1,) + digits + (1,)

        if not any(base_prime(digits, base) for base in range(2, 11)):
            yield digits

n = int(input())
for i in range(n):
    inp = str(input())
    print('Case #' + str(i+1) + ':\n'.format(i+1))

    bdigits, num_results = map(int, inp.split())
    for digits in islice(jamcoins(bdigits), 0, num_results):
        print(''.join(map(str, digits)),  end="")
        for base in range(2, 11):
            num = make_num(digits, base)
            print(' ' + str(divisor(num)), end="")
        print()