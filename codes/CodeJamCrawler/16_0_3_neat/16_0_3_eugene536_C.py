from math import *
import sys

sys.stdin = open("in", "r")
sys.stdout = open("out", "w")

primes = []
def getPrimes():
    global primes
    cnt = 70000
    for i in range(2, cnt):
        isPrime = True
        for j in primes:
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)


def getDivisor(x):
    st = int(sqrt(x)) + 1
    for p in primes:
        if p > st: 
            break
        if x % p == 0:
            return p
    return -1

def nextS(s):
    i = len(s) - 2;
    while i >= 0:
        if s[i] == '1':
            s[i] = '0'
        else:
            break
        i -= 1
    assert i > 0
    s[i] = '1'


getPrimes()
t, n, j = map(int, sys.stdin.read().split())

print("Case #1:")
s = list("1" + "0" * (n - 2) + "1")
while j > 0:
    str_ = "".join(s)
    res = []
    for k in range(2, 11):
        num = int(str_, k)
        res.append(getDivisor(num))
        if res[-1] == -1:
            res.pop()
            break
    if len(res) == 9:
        print(str_, end = " ")
        for x in res:
            print(x, end = " ")
        print()
        j -= 1
        print(j, file=sys.stderr)
    nextS(s)

