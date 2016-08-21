# Coin Jam

def coinjam(n, j):
    coin = [1] + [0] * (n - 2) + [1]
    primes = range(2, 100)
    while j > 0:
        try:
            div = [find_divisable(coin, base, primes) for base in range(2, 11)]
            print "".join(map(str, reversed(coin))), " ".join(map(str, div))
            j -= 1
        except:
            pass
        coin = next_coin(coin)

def find_divisable(coin, base, primes):
    for p in primes:
        if is_divisable(coin, base, p):
            return p
    raise Exception()

def is_divisable(coin, base, d):
    m, s = (0, 1)
    for c in coin:
        m = (m + s * c) % d
        s = (s * base) % d
    return m == 0

def next_coin(coin):
    i = coin.index(0)
    return [1] + [0] * (i - 1) + [1] + coin[i + 1:]

cases = int(raw_input())
for case in range(1, cases + 1):
    print "Case #" + str(case) + ":"
    n, j = map(int, raw_input().split(' '))
    coinjam(n, j)

