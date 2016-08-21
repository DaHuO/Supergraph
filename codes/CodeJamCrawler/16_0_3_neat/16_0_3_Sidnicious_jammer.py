from itertools import islice
from math import sqrt

# https://stackoverflow.com/a/12273111/84745
def any_divisor(x):
    i = 2
    limit = sqrt(x)
    while i * i <= limit:
        if x % i:
            i += 1
        else:
            return i

def gen_coins(n):
    base_coin = (1 << (n-1)) | 1
    for i in range(pow(2, n-2)):
        coin_str = "{:b}".format(base_coin | i << 1)
        factors = []
        for base in range(2, 11):
            num = int(coin_str, base)
            divisor = any_divisor(num)
            if divisor is None: break
            factors.append(divisor)
        else:
            yield coin_str, factors

for case in range(int(input())):
    n, j = map(int, input().split())
    print("Case #{}:".format(case+1))
    for coin, factors in islice(gen_coins(n), 0, j):
        print(coin, ' '.join(map(str, factors)))
