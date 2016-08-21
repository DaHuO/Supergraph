import sys
from math import sqrt

filename = sys.argv[1]

def read_num_cases(f):
    return int(f.readline().strip())

def read_case(f):
    return [int(n) for n in f.readline().strip().split(" ")]

def divisor(n):
    if n <= 2:
        return None
    rt = int(sqrt(n))
    i = 2
    while i < rt:
        if n % i == 0:
            return i
        i += 1
    return None

def jamcoins(N, J):
    l = N - 2
    ans = []
    for i in range(2 ** l):
        middle = bin(i)[2:]
        pad = '0' * (l - len(middle))
        coin = '1' + pad + middle + '1'
        current = [coin]
        for b in range(2,11):
            val = int(coin, b)
            d = divisor(val)
            if d is None:
                break
            current.append(d)
        else:
            ans.append(current)
            if len(ans) >= J:
                break
    return ans

with open(filename, 'r') as f:
    num_cases = read_num_cases(f)
    for case in xrange(num_cases):
        N, J = read_case(f)
        coins = jamcoins(N, J)
        print("Case #{}:".format(case + 1))
        for c in coins:
            print(" ".join([str(i) for i in c]))
