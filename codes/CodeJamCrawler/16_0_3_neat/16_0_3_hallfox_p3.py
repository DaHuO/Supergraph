import math


def is_prime(n):
    if n % 2 == 0:
        return 2
    for i in range(3, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return 1


def jamcoin_gen(n):
    coin = '1' + (n-2)*'0' + '1'
    while len(coin) == n:
        yield coin
        coin = "{:b}".format(int(coin, 2) + 2)


def solve(n, j):
    jamcoins = []
    for coin in jamcoin_gen(n):
        res = []
        for base in range(2, 11):
            d = is_prime(int(coin, base))
            if d == 1:
                break
            res.append(d)
        if len(res) == 9:
            # print(coin, res)
            jamcoins.append(coin + " " + " ".join(map(str, res)))
        if len(jamcoins) == j:
            return "\n".join(jamcoins)
    assert False


n = int(input())
for i in range(n):
    print("Case #{}:".format(i+1))
    print(solve(*[int(x) for x in input().strip().split()]))
