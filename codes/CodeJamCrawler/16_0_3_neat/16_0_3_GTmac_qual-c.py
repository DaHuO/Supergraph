import math

def get_primes(n):
    prime_list = []
    primes = {x: True for x in range(2, n + 1)}
    factors = {}
    for i in range(2, n + 1):
        if primes[i] is True:
            prime_list.append(i)
            for j in range(i * 2, n + 1, i):
                primes[j] = False
                factors[j] = i
    return prime_list, primes, factors

def get_val(coin, base, mod):
    val = 0
    for digit in coin:
        val = (base * val + digit) % mod
    return val

def val_to_bits(n, k):
    bits = [0 for i in range(k)]
    for i in range(k):
        bits[k - i - 1] = n % 2
        n /= 2
    return bits

def is_jamcoin(coin):
    factors = []
    for base in range(2, 11):
        is_valid = False
        for mod in [2, 3, 5, 7, 11]:
            if get_val(coin, base, mod) == 0:
                is_valid = True
                factors.append(mod)
                break
        if not is_valid:
            return False, []
    return True, factors

t = int(raw_input())

for case_num in range(1, t + 1):
    n, j = raw_input().split()
    n, j = int(n), int(j)

    print 'Case #%d:' % case_num
    coin_count = 0
    for x in xrange(2 ** (n - 1) + 1, 2 ** n, 2):
        bits = val_to_bits(x, n)
        str_bits = [str(bit) for bit in bits]
        if sum(bits) % 2 != 0:
            continue
        is_coin, f = is_jamcoin(bits)
        if is_coin:
            print ''.join(str_bits),
            for ff in f:
                print ff,
            print ''
            coin_count += 1
            if coin_count == j:
                break
