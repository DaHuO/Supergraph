from __future__ import print_function

import sys

import gmpy

def is_prime(num):
    if gmpy.is_prime(num) > 0:
        return (True, num)
    for i in range(2,num):
        if (num % i) == 0:
            return (False, i)
        if i > 1000000:
            return (True, num)

def is_jamcoin(num):
    string = str(num) if isinstance(num, int) else num
    if string.replace('0','').replace('1',''):
        return False
    if string[0] != '1' or string[-1] != '1':
        return False
    divisors = []
    for i in range(2,11):
        base = int(string, i)
        prime, divisor = is_prime(base)
        if prime:
            return False
        else:
            divisors.append(divisor)
    return divisors

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        count = int(f.readline())
        cases = [c.strip() for c in f.readlines()]
        for i in range(count):
            print("Case #{}:".format(i+1))
            size, result_count = cases[i].split()
            start = int('1' + '0'*(int(size)-2) + '1', 2)
            stop = int('1'*int(size), 2)
            results = 0
            for i in range(start, stop + 1, 2):
                num = gmpy.digits(i, 2)
                divisors = is_jamcoin(num)
                if not divisors:
                    continue
                print(num, end=' ')
                for d in divisors:
                    print(d, end=' ')
                print()
                results = results + 1
                if results >= int(result_count):
                    exit(0)

