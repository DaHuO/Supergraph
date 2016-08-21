#!/usr/bin/env python3

n = 32
j = 500
max_prime = 50

def is_unprime(n):
    if (n < 2):
        return n
    if (n == 2):
        return 0
    if (not (n % 2)):
        return 2
    for t in range(3, max_prime, 2):
        if (not(n % t)):
            return t
    return 0

def gen_string(i):
    l = bin(i)[2:]
    return '1' + (30 - len(l)) * '0' + l + '1'

def main():
    i = 0
    n = 0
    print("Case #1:")
    while (n < j):
        s = gen_string(i)
        t = 0
        c = [None] * 11
        for k in range(2, 11):
            a = int(s,k)
            b = is_unprime(a)
            c[k] = b
            t |= bool(b) << k
        if (t == 0x7FC):
            n += 1
            print('{0} {1} {2} {3} {4} {5} {6} {7} {8} {9}'.format(s, c[2], c[3], c[4], c[5], c[6], c[7], c[8], c[9], c[10]))
        i += 1

if __name__ == "__main__":
    main()
