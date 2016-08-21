import sys
import random
import threading
sys.setrecursionlimit(3000)


def enum(n):
    for i in range(2 **(n-2)):
        yield i * 2 + 1 + 2**(n-1)

def convert(n, a):
    if a == 2:
        return n
    res = 0
    m = 1
    while n > 0:
        res += (n % 2) * m
        n //= 2
        m *= a
    return res

cache = {}

prime = [2,3,5, 7, 11]

def isprime(n):
    for x in prime:
        if x * x > n:
            return True
        if n % x == 0:
            return False


def nextprime(n):
    while True:
        n = n + 2
        if isprime(n):
            return n


def enumprime(n):
    for x in prime:
        if x * x > n:
            return
        yield x

    while True:
        x = prime[-1]
        x = nextprime(x)
        prime.append(x)
        if x * x <= n:
            yield x
        else:
            break




def foo(n):
    for x in enumprime(n):
        if n % x == 0:
            return x
    return None

def notprime(n):
    if n not in cache:
        cache[n] = foo(n)
    return cache[n]


def q4(x):
    a = []
    for i in range(2, 11):
        a2 = convert(x, i)
        res = notprime(a2)
        if res is None:
            return None
        a.append(res)
    return str(convert(x, 10)) + ' ' +  ' '.join([str(x) for x in a])




def q3(n, j):
    print 'Case #1:'
    count = 0
    for x in enum(n):
        res = q4(x)
        if res is not None:
            count += 1
            print res
            if count >= j:
                break


def main():
    n = 16
    j = 50
    return q3(n, j)


main()

