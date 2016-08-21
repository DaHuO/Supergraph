#!/usr/bin/python3

def read(): return tuple(map(int, input().split()))

def check(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return n // i
        i += 1
    return 0

def solve():
    n, j = read()
    for _ in range(2**(n - 1) + 1, 2 ** n, 2):
        b = bin(_)[2:]
        var = [check(int(b, base)) for base in range(2, 11)]
        if 0 not in var:
            j -= 1
            print(b, *var)
        if not j:
            break

if __name__ == '__main__':
    for _ in range(int(input())):
        print('Case #%i:' % (_ + 1))
        solve()
